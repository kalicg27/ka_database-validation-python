import os
import sys
import psycopg2
import pytest
from src.db.config import DBConfig


# -------------------------------------------------------------
# Ensure project root is added to sys.path so "src" is importable
# -------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def run_sql_file(cursor, path: str):
    """Utility to execute an SQL file."""
    with open(path, "r", encoding="utf-8") as f:
        cursor.execute(f.read())


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    """
    Automatically runs before the test session.
    Loads the schema and seed data into PostgreSQL.
    Works locally and in GitHub Actions.
    """
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
        cursor = conn.cursor()

        base_dir = os.path.dirname(os.path.dirname(__file__))
        schema_file = os.path.join(base_dir, "sql", "create_schema.sql")
        seed_file = os.path.join(base_dir, "sql", "seed_data.sql")

        run_sql_file(cursor, schema_file)
        run_sql_file(cursor, seed_file)

        cursor.close()
    finally:
        conn.close()
