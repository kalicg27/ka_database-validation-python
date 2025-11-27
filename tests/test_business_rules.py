from src.validation.rules_business import (
    customers_without_orders,
    orders_with_invalid_total_quantity,
)

def test_all_customers_have_at_least_one_order():
    assert customers_without_orders() == 0


def test_no_orders_with_invalid_quantity():
    assert orders_with_invalid_total_quantity() == 0
