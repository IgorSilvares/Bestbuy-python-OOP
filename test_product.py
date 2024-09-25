import pytest
from products import Product

def test_create_normal_product():
    product = Product("Test Product", 10.99, 5)
    assert product.name == "Test Product"
    assert product.price == 10.99
    assert product.quantity == 5
    assert product.is_active()


def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", 10.99, 5)
    with pytest.raises(ValueError):
        Product("Test Product", 0, 5)
    with pytest.raises(ValueError):
        Product("Test Product", -10.99, 2)


def test_product_becomes_inactive_when_quantity_becomes_zero():
    product = Product("Test Product", 10.99, 5)
    product.buy(5)
    assert not product.is_active()


def test_buying_more_than_available_quantity():
    product = Product("Test Product", 10.99, 5)
    with pytest.raises(ValueError):
        product.buy(6)

