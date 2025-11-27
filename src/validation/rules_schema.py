from src.db.client import fetch_all

def expected_tables() -> set[str]:
    return {"customers", "products", "orders", "order_items"}


def get_tables_in_db() -> set[str]:
    rows = fetch_all("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)
    return {r[0] for r in rows}


def get_columns_for_table(table_name: str) -> dict[str, str]:
    rows = fetch_all("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public' AND table_name = %s;
    """, (table_name,))
    return {name: dtype for name, dtype in rows}
