import os
import json
from asyncpg import create_pool, connect, Connection
from asyncpg.pool import Pool


async def get(user: str = os.environ["PG_USER"], password: str = os.environ["PG_PASSWORD"],
              database: str = os.environ["PG_DATABASE"], host: str = os.environ["PG_HOST"],
              port: int = os.environ["PG_PORT"]) -> Connection:
    connection: Connection = await connect(user=user, password=password, database=database, host=host, port=port)
    await __init(connection)
    return connection


async def get_pool(user: str = os.environ["PG_USER"], password: str = os.environ["PG_PASSWORD"],
                   database: str = os.environ["PG_DATABASE"], host: str = os.environ["PG_HOST"],
                   port: int = os.environ["PG_PORT"], min_size: int = 0,
                   max_size: int = 2, max_inactive_connection_lifetime: int = 2) -> Pool:
    return await create_pool(user=user, password=password, database=database, host=host, port=port,
                             min_size=min_size, max_size=max_size,
                             max_inactive_connection_lifetime=max_inactive_connection_lifetime,
                             init=__init)


async def __init(conn: Connection):
    await conn.set_type_codec("uuid", encoder=str, decoder=str, schema="pg_catalog")
    await conn.set_type_codec("numeric", encoder=str, decoder=float, schema="pg_catalog")
    await conn.set_type_codec("jsonb", encoder=json.dumps, decoder=json.loads, schema="pg_catalog")
