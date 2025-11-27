from src.validation.rules_data_quality import (
    count_nulls, count_duplicates, count_negative_prices
)

def test_no_null_emails_in_customers():
    assert count_nulls("customers", "email") == 0


def test_no_duplicate_customer_emails():
    assert count_duplicates("customers", "email") == 0


def test_no_negative_product_prices():
    assert count_negative_prices() == 0
