from src.db.client import fetch_all

def count_nulls(table: str, column: str) -> int:
    rows = fetch_all(
        f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL;"
    )
    return rows[0][0]


def count_duplicates(table: str, column: str) -> int:
    rows = fetch_all(
        f"""
        SELECT COUNT(*) FROM (
            SELECT {column}, COUNT(*)
            FROM {table}
            GROUP BY {column}
            HAVING COUNT(*) > 1
        ) AS dup;
        """
    )
    return rows[0][0]


def count_negative_prices() -> int:
    rows = fetch_all(
        "SELECT COUNT(*) FROM products WHERE price_cents <= 0;"
    )
    return rows[0][0]
