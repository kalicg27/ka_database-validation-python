from src.db.client import fetch_all

def customers_without_orders() -> int:
    rows = fetch_all("""
        SELECT COUNT(*)
        FROM customers c
        LEFT JOIN orders o ON o.customer_id = c.id
        WHERE o.id IS NULL;
    """)
    return rows[0][0]


def orders_with_invalid_total_quantity() -> int:
    """
    Example check: quantity must be > 0 (already in DB constraint),
    here we can add more complex rules later.
    """
    rows = fetch_all("""
        SELECT COUNT(*)
        FROM order_items
        WHERE quantity <= 0;
    """)
    return rows[0][0]
