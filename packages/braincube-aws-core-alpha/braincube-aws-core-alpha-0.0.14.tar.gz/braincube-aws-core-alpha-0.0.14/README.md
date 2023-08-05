# sam-api

### Requirements

To use the SAM CLI, you need the following tools.

* [SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3](https://www.python.org/downloads/)
* [Docker](https://hub.docker.com/search/?type=edition&offering=community)

### Run server locally

```bash
# open ssh tunel
sudo sh ssh_tunnel_Analog_JBox.sh
# apply code changes to docker image
sam-api$ sam build
# start server locally on http://127.0.0.1:3000
sam-api$ sam local start-api --warm-containers EAGER
# or run function locally using event.json as parameter
sam-api$ sam local invoke ApiFunction --event events/event.json
```

### Deploy to AWS

```bash
sam build --use-container
sam deploy --guided --profile analog_user --region eu-west-1
```

### PostgresRepository usage

```python
from core.rest.data import HTTPRequest
from core.utils.data import Order, OrderType
from core.dal.data import Key, Schema, Column, Relation, SimpleColumn, JoinType, JoinThrough, StatementField
from core.dal.postgres_connection import get_pool, Pool
from core.dal.postgres_repository import PostgresRepository

# schema definition
equities = Schema(
    table="equities",
    alias="e",
    primary_key=["id"],
    order=[Order(type=OrderType.asc, alias="name")],
    statement_fields=[
        StatementField(alias="isTypeOne",
                       statement="CASE WHEN e.type = 1 then True else False END",
                       relations_aliases=[])
    ],
    columns=[
        Column(name="id", updatable=False, insertable=False),
        Column(name="name"),
        Column(name="type"),
        Column(name="issuer_id", alias="issuerId"),
        Column(name="industry_sector", alias="industrySector"),
        Column(name="isin"),
        Column(name="reference"),
        Column(name="bloomberg_code", alias="bloombergCode"),
        Column(name="market_symbol", alias="marketSymbol"),
        Column(name="currency"),
        Column(name="country", ),
        Column(name="min_amount", alias="minAmount"),
    ],
    relations=[
        Relation(
            table="parties",
            alias="p",
            force_join=False,
            columns=[
                SimpleColumn(name="name"),
                SimpleColumn(name="short_name", alias="shortName"),
            ],
            join_type=JoinType.left,
            through=JoinThrough(from_column_name="issuer_id", to_column_name="id")
        )
    ]
)


# repository definition
class EquitiesRepo(PostgresRepository):

    def __init__(self, pool: Pool):
        super().__init__(pool, equities)


# repository usage

request = HTTPRequest()

repo = EquitiesRepo(await get_pool())

await repo.find_by_id(key=Key(request.path_parameters["id"]), aliases=request.query_parameters.fields)

await repo.exists_by_id(key=Key("9448a57b-f686-4935-b152-566baab712db"))

await repo.find_one(
    aliases=request.query_parameters.fields,
    conditions=request.query_parameters.conditions,
    order=request.query_parameters.order)

await repo.find_all(
    aliases=request.query_parameters.fields,
    conditions=request.query_parameters.conditions,
    order=request.query_parameters.order)

await repo.find_all_by_id([
    Key("9448a57b-f686-4935-b152-566baab712db"),
    Key("43c8ec37-9a59-44eb-be90-def391ba2f02")],
    aliases=request.query_parameters.fields,
    order=request.query_parameters.order)

await repo.find_all_page(
    aliases=request.query_parameters.fields,
    conditions=request.query_parameters.conditions,
    page=request.query_parameters.page,
    order=request.query_parameters.order)

await repo.insert(
    data={
        "name": "Bursa de Valori Bucuresti SA",
        "type": 1,
        "industrySector": 40,
        "isin": "ROBVBAACNOR0",
        "bloombergCode": "BBG000BBWMC5",
        "marketSymbol": "BVB RO Equity",
        "currency": "RON",
        "country": "RO",
    })

await repo.insert_bulk(
    aliases=["name", "type", "industrySector", "isin", "bloombergCode", "marketSymbol", "currency", "country"],
    data=[
        ["Bursa de Valori Bucuresti SA", 1, 40, "ROBVBAACNOR0", "BBG000BBWMC5", "BVB RO Equity", "RON", "RO"],
        ["Citigroup Inc", 1, 40, "US1729674242", "BBG000FY4S11", "C US Equity", "USD", "US"],
        ["Coca-Cola HBC AG", 1, 49, "CH0198251305", "BBG004HJV2T1", "EEE GA Equity", "EUR", "GR"],
    ]
)

await repo.update(
    data={
        "type": 1,
        "isin": 40,
    },
    conditions=request.query_parameters.conditions,
    returning_aliases=request.query_parameters.fields)

await repo.update_by_id(
    Key("9448a57b-f686-4935-b152-566baab712db"),
    data={
        "type": 1,
        "isin": 40,
    }, returning_aliases=[])

await repo.delete(
    conditions=request.query_parameters.conditions,
    returning_aliases=["id", "name", "type"])

await repo.delete_by_id(
    Key("9448a57b-f686-4935-b152-566baab712db"),
    returning_aliases=["id", "name", "type"])

await repo.fetch_raw("SELECT * FROM equities WHERE type = $1 and isin = $2", [1, "TREEGYO00017"])

await repo.fetch_one_raw("SELECT * FROM equities WHERE id = $1", ["2b67122a-f47e-41b1-b7f7-53be5ca381a0"])

await repo.execute_raw("DELETE FROM equities WHERE id = $1", ["2b67122a-f47e-41b1-b7f7-53be5ca381a0"])

```

### Query params format

```
fields=name, type, industrySector, isin, bloombergCode, parties_name, parties_shortName

type=1
isin=range(40, 49)
id=any(9448a57b-f686-4935-b152-566baab712db, 43c8ec37-9a59-44eb-be90-def391ba2f02)

page_no=1
page_size=50
top_size=50
order=name, id DESC
```

### Build and deploy new package version using twine

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

```bash
python3 -m build
twine upload --skip-existing dist/*
```

### Resources

* [SAM template.yml](https://github.com/aws/serverless-application-model/blob/master/docs/internals/generated_resources.rst)
* [asyncpg driver](https://magicstack.github.io/asyncpg/current/)
* [PyPika query builder](https://pypika.readthedocs.io/en/latest/)
* [Pydantic](https://docs.pydantic.dev/)
