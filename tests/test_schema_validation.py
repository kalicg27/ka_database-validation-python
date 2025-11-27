from src.validation.rules_schema import get_tables_in_db, expected_tables, get_columns_for_table

def test_expected_tables_exist():
    tables = get_tables_in_db()
    assert expected_tables().issubset(tables)


def test_customers_table_columns():
    columns = get_columns_for_table("customers")
    expected = {"id", "email", "country", "created_at"}
    assert expected.issubset(set(columns.keys()))
