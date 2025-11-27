import psycopg2
from contextlib import contextmanager
from .config import DBConfig

@contextmanager
def db_connection():
    config = DBConfig.from_env()
    conn = psycopg2.connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        dbname=config.dbname,
    )
    try:
        yield conn
    finally:
        conn.close()


def fetch_all(query: str, params: tuple | None = None) -> list[tuple]:
    with db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            return cur.fetchall()
