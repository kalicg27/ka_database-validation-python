import os
import sys

# -------------------------------------------------------------------
# Ensure project root (the folder that contains "src/") is on sys.path
# -------------------------------------------------------------------
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import psycopg2
import pytest
from src.db.config import DBConfig


def run_sql_file(cursor, path: str) -> None:
    """Execute all statements from an SQL file."""
    with open(path, "r", encoding="utf-8") as f:
        cursor.execute(f.read())


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    """
    Session-scoped fixture that prepares the database before any tests run.

    It:
    - Connects to PostgreSQL using DBConfig.from_env()
    - Executes sql/create_schema.sql
    - Executes sql/seed_data.sql
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

        base_dir = ROOT_DIR  # project root
        schema_file = os.path.join(b_
