import pytest

import products
import store


def test_creating_normal_product():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose is not None
    assert bose.name == "Bose QuietComfort Earbuds"
    assert bose.price == 250
    assert bose.quantity == 500


def test_creating_product_with_invalid_details():
    with pytest.raises(Exception, match="Name is empty or price or quantity is negative."):
        bose = products.Product("", price=250, quantity=500)


def test_product_reaches_zero_quantity_flag_goes_inactive():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100)]
    best_buy = store.Store(product_list)
    best_buy.order(product_list[0], 100)
    assert product_list[0].active is False


def test_product_order_changes_quantity():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100)]
    best_buy = store.Store(product_list)
    best_buy.order(product_list[0], 50)
    assert product_list[0].quantity == 50


def test_product_order_more_than_quantity_triggers_exception():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100)]
    best_buy = store.Store(product_list)
    with pytest.raises(Exception, match="Error while making order! Quantity larger than what exists."):
        best_buy.order(product_list[0], 120)
