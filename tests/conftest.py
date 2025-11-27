import os
import psycopg2
import pytest
from src.db.config import DBConfig

def run_sql_file(cursor, path: str):
    with open(path, "r", encoding="utf-8") as f:
        cursor.execute(f.read())


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    config = DBConfig.from_env()
    conn = psycopg2.connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        dbname=config.dbname,
    )
    conn.autocommit = True
    try:
        cur = conn.cursor()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        run_sql_file(cur, os.path.join(base_dir, "sql", "create_schema.sql"))
        run_sql_file(cur, os.path.join(base_dir, "sql", "seed_data.sql"))
        cur.close()
    finally:
        conn.close()
