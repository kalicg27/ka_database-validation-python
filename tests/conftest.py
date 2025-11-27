import os
import sys
import psycopg2
import pytest

# -------------------------------------------------------------------
# Ensure project root (folder that contains "src/" and "sql/") is on sys.path
# -------------------------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.db.config import DBConfig


def run_sql_file(cursor, path: str) -> None:
    """Execute all statements in an SQL file."""
    with open(path, "r", encoding="utf-8") as f:
        cursor.execute(f.read())


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    """
    Session-scoped fixture that prepares the database before any tests run.

    Steps:
    - Connect to PostgreSQL using environment variables via DBConfig.
    - Execute sql/create_schema.sql to create tables.
    - Execute sql/seed_data.sql to insert initial data.
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

        # Paths to SQL files relative to project root
        schema_file = os.path.join(ROOT_DIR, "sql", "create_schema.sql")
        seed_file = os.path.join(ROOT_DIR, "sql", "seed_data.sql")

        run_sql_file(cursor, schema_file)
        run_sql_file(cursor, seed_file)

        cursor.close()
    finally:
        conn.close()
