import time
import math
import itertools
from typing import Optional, List, Dict, Union, Tuple

from pypika import PostgreSQLQuery, Table, Field, Criterion, EmptyCriterion, CustomFunction, functions as fn
from pypika.queries import QueryBuilder

from ..utils.data import Order, OrderType, Condition, ConditionType, Page, Pageable, Paging, Top, Metadata
from .data import Key, Schema, Relation, SaveType, Column, StatementField
from .database_errors import DatabaseError, DeleteError, SaveError
from .postgres_connection import Pool, Connection


class PostgresRepository:
    """SQL based repository implementation.
    :param pool: database connection pool
    :param schema: representation of master and related tables including columns, sub-queries and storage restrictions
    :param relation_separator: character that will be used in order to separate related tables from each column
    """

    def __init__(self, pool: Pool, schema: Schema, relation_separator: str = "_"):
        self._pool = pool
        self._relation_separator = relation_separator
        self.__construct_schema_data(schema)

    def __construct_schema_data(self, schema: Schema):

        # master table definition:
        self._master_table: Tuple[Table, str] = \
            Table(schema.table).as_(schema.alias) if schema.alias else Table(schema.table), schema.table

        self._master_columns: Dict[str, Tuple[Field, Column]] = dict(
            map(lambda c: (c.alias if c.alias else c.name, (
                (self._master_table[0][c.name]).as_(c.alias) if c.alias else self._master_table[0][c.name], c)),
                schema.columns))

        self._master_statement_fields: Dict[str, Tuple[Field, StatementField]] = dict(
            map(lambda f: (f.alias, (self._master_table[0][f.alias], f)), schema.statement_fields))

        self._master_primary_key: Dict[str, Tuple[Field, Column]] = dict(
            itertools.islice(self._master_columns.items(), len(schema.primary_key)))

        # related tables definition:
        self._related_tables: Dict[str, Tuple[Table, Relation]] = dict()
        self._related_columns: Dict[str, Tuple[Field]] = dict()
        self._related_forced_tables_aliases: List[str] = list()

        for relation in schema.relations:
            table_alias = relation.alias if relation.alias else relation.table
            related_table = Table(relation.table).as_(relation.alias) if relation.alias else Table(relation.table)
            self._related_tables[table_alias] = related_table, relation
            if relation.force_join:
                self._related_forced_tables_aliases.append(table_alias)
            for column in relation.columns:
                column_alias = \
                    f"{relation.table}{self._relation_separator}{column.alias if column.alias else column.name}"
                self._related_columns[column_alias] = (related_table[column.name]).as_(column_alias),

        self._schema_columns: Dict[str, tuple] = {**self._master_columns, **self._related_columns}
        self._schema_columns_fields: Dict[str, tuple] = {**self._schema_columns, **self._master_statement_fields}

        # order by definition:
        self._schema_order: List[Tuple[Field, OrderType]] = [(self._schema_columns_fields[order.alias][0], order.type)
                                                             for order in schema.order]

    async def fetch_raw(self, q: str, params: Optional[list] = None, connection: Optional[Connection] = None):
        """Retrieve records from raw PSQL query.
        :param q: Query.
        :param params: Query parameters.
        :param connection: (asyncpg) Connection that will execute the query.
        :return: Records as dictionary.
        """

        try:
            print(f"query:: {q}")
            if connection:
                return [dict(r) for r in (await connection.fetch(q, *params) if params else await connection.fetch(q))]
            async with self._pool.acquire() as connection_:
                return [dict(r) for r in
                        (await connection_.fetch(q, *params) if params else await connection_.fetch(q))]
        except Exception as e:
            raise DatabaseError(e)

    async def fetch_one_raw(self, q: str,
                            params: Optional[list] = None,
                            connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:
        """Retrieve record from raw PSQL query.
        :param q: Query.
        :param params: Query parameters.
        :param connection: (asyncpg) Connection that will execute the query.
        :return: Record as dictionary.
        """

        data = await self.fetch_raw(q, params, connection)

        return data[0] if data else None

    async def execute_raw(self, q: str, params: Optional[list] = None, connection: Optional[Connection] = None) -> any:
        """Execute raw PSQL query.
        :param q: Query.
        :param params: Query parameters.
        :param connection: (asyncpg) Connection that will execute the query.
        :return: Execution results as dictionary.
        """

        return await self.fetch_raw(q, params, connection)

    async def _fetch(self, q: QueryBuilder,
                     replace_fields=True,
                     connection: Optional[Connection] = None) -> List[Dict[str, any]]:

        query = self._replace_statement_fields(q) if replace_fields else str(q)

        return await self.fetch_raw(query, connection=connection)

    async def _fetch_one(self, q: QueryBuilder,
                         replace_fields=True,
                         connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:

        data = await self._fetch(q, replace_fields, connection)

        return data[0] if data else None

    async def _execute(self, q: QueryBuilder,
                       returning_aliases: Optional[List[str]] = None,
                       connection: Optional[Connection] = None) -> any:

        table = Table(self._master_table[1])

        for field, column in self._aliases_to_fields(returning_aliases, select=False):
            q = q.returning(table[field.name].as_(field.alias))

        return await self._fetch(q, False, connection)

    def _create_primary_key_criterion(self, key: Key) -> Criterion:

        return Criterion.all([
            pk[0] == key.values[i] for i, pk in enumerate(self._master_primary_key.values())
        ])

    def _aliases_to_fields(self, aliases: Optional[List[str]] = None, select: bool = True) -> List[tuple]:

        fields = list()
        accepted = self._schema_columns_fields if select else self._master_columns
        if aliases:
            for alias in aliases:
                field = accepted.get(alias)
                if not field:
                    continue
                fields.append(field)

        return fields if fields else list(
            self._master_columns.values() if select else self._master_primary_key.values())

    def _order_to_fields(self, order: List[Order]) -> List[Tuple[Field, OrderType]]:

        data = list()
        for order_ in order:
            field = self._schema_columns_fields.get(order_.alias)
            if not field:
                continue
            data.append((field[0], order_.type))

        return data if data else self._schema_order

    def _conditions_to_criterion(self, conditions: Optional[List[Condition]] = None, select: bool = True) -> Criterion:

        if not conditions:
            return EmptyCriterion()

        criteria = list()
        for con in conditions:
            column = self._schema_columns.get(con.alias)
            if not column:
                continue
            field = column[0] if select else Field(name=column[0].name)
            if isinstance(con.value, list):
                if con.type == ConditionType.range:
                    if con.value[0]:
                        criteria.append(con.value[0] <= field)
                    if con.value[1]:
                        criteria.append(field <= con.value[1])
                elif con.type == ConditionType.any:
                    any_func = CustomFunction("any", ["p1"])
                    criteria.append(field == any_func(con.value))
            else:
                criteria.append(field == con.value)

        return Criterion.all(criteria)

    def _replace_statement_fields(self, q: QueryBuilder) -> str:

        query = str(q)

        for field, schema_field in self._master_statement_fields.values():
            query = query.replace(f"\"{self._master_table[0].alias}\".\"{field.name}\"",
                                  f"{schema_field.statement} \"{field.name}\"")

        return query

    def _filter_save_data(self, data: Dict[str, any], type_: SaveType) -> Dict[str, any]:

        data_: Dict[str, any] = dict()

        for k, v in data.items():
            column = self._master_columns.get(k)
            if not column:
                continue
            if type_ == SaveType.insert and not column[1].insertable:
                raise SaveError(f"column:'{column[1].name}' is not insertable", column[1].name)
            if type_ == SaveType.update and not column[1].updatable:
                raise SaveError(f"column:'{column[1].name}' is not updatable", column[1].name)
            data_[column[1].name] = v

        if not data_:
            raise SaveError("no columns provided")

        return data_

    def __init_select_query(self, fields: List[tuple],
                            criterion: Optional[Criterion] = None,
                            order: Optional[List[Tuple[Field, OrderType]]] = None,
                            count_query: bool = False) -> Tuple[QueryBuilder, Optional[QueryBuilder]]:

        q = PostgreSQLQuery.from_(self._master_table[0])

        table_aliases = self._related_forced_tables_aliases.copy()

        for field in fields:
            if len(field) == 2 and isinstance(field[1], StatementField):
                table_aliases.extend(field[1].relations_aliases)
            else:
                table_aliases.append(field[0].table.alias)

        if criterion:
            table_aliases.extend([t.alias for t in criterion.tables_])
            q = q.where(criterion)

        if order:
            table_aliases.extend([o[0].table.alias for o in order])

        for alias in filter(lambda ta: ta != self._master_table[0].alias, set(table_aliases)):
            table, relation = self._related_tables[alias]
            q = q \
                .join(table, relation.join_type) \
                .on(self._master_table[0][relation.through.from_column_name] == table[relation.through.to_column_name])

        cq = q.select(fn.Count("*")) if count_query else None

        for field in fields:
            q = q.select(field[0])

        if order:
            for field, type_ in order:
                q = q.orderby(field, order=type_)

        return q, cq

    def _init_select_query(self, aliases: Optional[List[str]] = None,
                           criterion: Optional[Criterion] = None,
                           order: Optional[List[Order]] = None,
                           set_order: bool = True,
                           count_query: bool = False) -> Tuple[QueryBuilder, Optional[QueryBuilder]]:

        fields = self._aliases_to_fields(aliases)
        order_ = self._order_to_fields(order) if order else (self._schema_order if set_order else None)

        return self.__init_select_query(fields, criterion, order_, count_query)

    async def _find_one(self, aliases: Optional[List[str]] = None,
                        criterion: Optional[Criterion] = None,
                        order: Optional[List[Order]] = None,
                        connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:

        q, _ = self._init_select_query(aliases, criterion, order)

        return await self._fetch_one(q.limit(1), connection=connection)

    async def _find_all(self, aliases: Optional[List[str]] = None,
                        criterion: Optional[Criterion] = None,
                        order: Optional[List[Order]] = None,
                        connection: Optional[Connection] = None) -> List[Dict[str, any]]:

        q, _ = self._init_select_query(aliases, criterion, order)

        return await self._fetch(q, connection=connection)

    async def _find_all_page(self, connection: Connection,
                             aliases: Optional[List[str]] = None,
                             criterion: Optional[Criterion] = None,
                             page: Pageable = Pageable(),
                             order: Optional[List[Order]] = None) -> Union[Page, Top]:

        start = time.time()

        calc_top = page.top_size > 0
        q, cq = self._init_select_query(aliases, criterion, order, count_query=not calc_top)

        # top implementation
        if calc_top:
            records = await self._fetch(q.limit(page.top_size + 1), connection=connection)
            has_more = len(records) > page.top_size
            return Top(records[:-1] if has_more else records, page.top_size, has_more)

        # paging implementation
        page_no = page.page_no if page.page_no > 0 else 1
        records = await self._fetch(q.limit(page.page_size).offset((page_no - 1) * page.page_size),
                                    connection=connection)

        # retrieve count only if we do not mention page ether we are not on
        # first page and there are no records from first retrieve
        count = None
        total_pages = None
        retrieve_pre_page = len(records) == 0 and page.page_no > 1

        if retrieve_pre_page or page.page_no == 0:
            record = await self._fetch_one(cq, connection=connection)
            count = record["count"] if record.get("count") else 0
            total_pages = math.ceil(count / page.page_size)

        if retrieve_pre_page and total_pages > 0:
            page_no = total_pages
            records = await self._fetch(q.limit(page.page_size).offset((page_no - 1) * page.page_size),
                                        connection=connection)

        return Page(records, Paging(page_no, page.page_size, total_pages, count),
                    Metadata(int((time.time() - start) * 1000)))

    async def _update(self, data: Dict[str, any],
                      criterion: Criterion,
                      returning_aliases: Optional[List[str]] = None,
                      connection: Optional[Connection] = None) -> Optional[List[Dict[str, any]]]:

        if isinstance(criterion, EmptyCriterion):
            raise SaveError("update without conditions is not allowed")

        uq = PostgreSQLQuery.update(self._master_table[1])

        for v, k in self._filter_save_data(data, SaveType.update).items():
            uq = uq.set(v, k)
        uq = uq.where(criterion)

        return await self._execute(uq, returning_aliases, connection)

    async def _delete(self, criterion: Criterion,
                      returning_aliases: Optional[List[str]] = None,
                      connection: Optional[Connection] = None) -> Optional[List[Dict[str, any]]]:

        if isinstance(criterion, EmptyCriterion):
            raise DeleteError("delete without conditions is not allowed")

        dq = PostgreSQLQuery \
            .from_(self._master_table[1]) \
            .delete() \
            .where(criterion)

        return await self._execute(dq, returning_aliases, connection)

    async def find_by_id(self, key: Key,
                         aliases: Optional[List[str]] = None,
                         connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:
        """Find the record from passed key.
        :param key: Record identifier.
        :param aliases: List of fields that will be selected by the query.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Record as dictionary.
        """

        criterion = self._create_primary_key_criterion(key)

        q, _ = self._init_select_query(aliases, criterion, set_order=False)

        return await self._fetch_one(q, connection=connection)

    async def exists_by_id(self, key: Key, connection: Optional[Connection] = None) -> bool:
        """Find if record exists from passed key.
        :param key: Record identifier.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Record existence.
        """

        aliases = [column.alias for field, column in self._master_primary_key.values()]

        return await self.find_by_id(key, aliases, connection) is not None

    async def find_one(self, aliases: Optional[List[str]] = None,
                       conditions: Optional[List[Condition]] = None,
                       order: Optional[List[Order]] = None,
                       connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:
        """Find one record from passed filters.
        :param aliases: List of fields that will be selected by the query.
        :param conditions: List of filters that will be applied to query.
        :param order: Order that will be applied to query.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Record as dictionary.
        """

        criterion = self._conditions_to_criterion(conditions)

        return await self._find_one(aliases, criterion, order, connection)

    async def find_all(self, aliases: Optional[List[str]] = None,
                       conditions: Optional[List[Condition]] = None,
                       order: Optional[List[Order]] = None,
                       connection: Optional[Connection] = None) -> List[Dict[str, any]]:
        """Find all records from passed filters.
        :param aliases: List of fields that will be selected by the query.
        :param conditions: List of filters that will be applied to query.
        :param order: Order in which the records will be returned.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Records as dictionary list.
        """

        criterion = self._conditions_to_criterion(conditions)

        return await self._find_all(aliases, criterion, order, connection)

    async def find_all_by_id(self, keys: List[Key],
                             aliases: Optional[List[str]] = None,
                             order: Optional[List[Order]] = None,
                             connection: Optional[Connection] = None) -> List[Dict[str, any]]:
        """Find all records from passed keys.
        :param keys: Records identifiers.
        :param aliases: List of fields that will be selected by the query.
        :param order: Order in which the records will be returned.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Record as dictionary.
        """

        if not keys:
            raise DatabaseError("no keys provided")

        criterion = Criterion.any([self._create_primary_key_criterion(key) for key in keys])

        return await self._find_all(aliases, criterion, order, connection)

    async def find_all_page(self, aliases: Optional[List[str]] = None,
                            conditions: Optional[List[Condition]] = None,
                            page: Pageable = Pageable(),
                            order: Optional[List[Order]] = None,
                            connection: Optional[Connection] = None) -> Union[Page, Top]:
        """Find records from passed filters using paging.
        :param aliases: List of fields that will be selected by the query.
        :param conditions: List of filters that will be applied to query.
        :param page: Limit and offset of the query.
        :param order: Order in which the records will be returned.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :return: Records wrapped by Page or Top dataclass.
        """

        criterion = self._conditions_to_criterion(conditions)

        if connection:
            return await self._find_all_page(connection, aliases, criterion, page, order)
        async with self._pool.acquire() as connection_:
            return await self._find_all_page(connection_, aliases, criterion, page, order)

    async def insert(self, data: Dict[str, any],
                     returning_aliases: Optional[List[str]] = None,
                     connection: Optional[Connection] = None) -> Dict[str, any]:
        """Insert one record from dictionary.
        :param data: Master column aliases with values.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When does not adjust to insert-constraints or no master column is specified.
        :return: Execution results as dictionary.
        """

        data_ = self._filter_save_data(data, SaveType.insert)

        iq = PostgreSQLQuery \
            .into(self._master_table[1]) \
            .columns(list(data_.keys())) \
            .insert(list(data_.values()))

        records = await self._execute(iq, returning_aliases, connection)

        return records[0] if len(records) > 0 else None

    async def insert_bulk(self, aliases: List[str],
                          data: List[List[any]],
                          returning_aliases: Optional[List[str]] = None,
                          connection: Optional[Connection] = None) -> List[Dict[str, any]]:
        """Insert many records at once from list.
        :param aliases: Master column aliases.
        :param data: Master column values.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When does not adjust to insert-constraints or no master column is specified.
        :return: Execution results as dictionary list.
        """

        for d in data:
            if len(d) == len(aliases):
                continue
            raise SaveError("invalid bulk insert data")

        column_names: Dict[str, int] = dict()
        for i, alias in enumerate(aliases):
            column = self._master_columns.get(alias)
            if not column:
                continue
            if not column[1].insertable:
                raise SaveError(f"column:'{column[1].name}' is not insertable", column[1].name)
            column_names[column[1].name] = i
        if not column_names:
            raise SaveError("no columns provided")

        iq = PostgreSQLQuery \
            .into(self._master_table[1]) \
            .columns(list(column_names.keys()))

        for d in data:
            iq = iq.insert([d[i] for i in column_names.values()])

        return await self._execute(iq, returning_aliases, connection)

    async def update(self, data: Dict[str, any],
                     conditions: List[Condition],
                     returning_aliases: Optional[List[str]] = None,
                     connection: Optional[Connection] = None) -> Optional[List[Dict[str, any]]]:
        """Update records with new data according conditions.
        :param data: Master column aliases with values.
        :param conditions: List of filters that will be applied into the query.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When does not adjust to update-constraints or no master column is specified.
        :return: Execution results as dictionary list.
        """

        criterion = self._conditions_to_criterion(conditions, select=False)

        return await self._update(data, criterion, returning_aliases, connection)

    async def update_by_id(self, key: Key,
                           data: Dict[str, any],
                           returning_aliases: Optional[List[str]] = None,
                           connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:
        """Update records with new data according to passed key.
        :param key: Record identifier.
        :param data: Master column aliases with values.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When does not adjust to update-constraints or no master column is specified.
        :return: Execution results as dictionary.
        """

        criterion = self._create_primary_key_criterion(key)

        records = await self._update(data, criterion, returning_aliases, connection)

        return records[0] if len(records) > 0 else None

    async def delete(self, conditions: List[Condition],
                     returning_aliases: Optional[List[str]] = None,
                     connection: Optional[Connection] = None) -> Optional[List[Dict[str, any]]]:
        """Delete records according conditions.
        :param conditions: List of filters that will be applied into the query.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When conditions are empty.
        :return: Execution results as dictionary list.
        """

        criterion = self._conditions_to_criterion(conditions, select=False)

        return await self._delete(criterion, returning_aliases, connection)

    async def delete_by_id(self, key: Key,
                           returning_aliases: Optional[List[str]] = None,
                           connection: Optional[Connection] = None) -> Optional[Dict[str, any]]:
        """Delete records according to passed key.
        :param key: Record identifier.
        :param returning_aliases: Query returning data.
        :param connection: (asyncpg) Connection that will execute the generated query.
        :raise SaveError: When conditions are empty.
        :return: Execution results as dictionary.
        """

        criterion = self._create_primary_key_criterion(key)

        records = await self._delete(criterion, returning_aliases, connection)

        return records[0] if len(records) > 0 else None
