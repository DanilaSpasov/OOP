import pytest

from src.Classes import Category
from src.Classes import Product


@pytest.fixture()
def tomato():
    return Product("tomato", "It's a tomato", 50, 1)


@pytest.fixture()
def vegetables(tomato):
    return Category("vegetables", "not fruits", [tomato])


@pytest.fixture(autouse=True)
def reset_count():
    Category.product_count = 0
    Category.category_count = 0


def test_init_Product(tomato):
    assert tomato.name == "tomato"
    assert tomato.description == "It's a tomato"
    assert tomato.price == 50
    assert tomato.quantity == 1


def test_init_Category(vegetables, tomato):
    assert vegetables.name == "vegetables"
    assert vegetables.description == "not fruits"
    assert vegetables.products == "tomato, 50 руб. Остаток: 1 шт."


def test_category_count(tomato, vegetables):
    assert Category.product_count == 1
    assert Category.category_count == 1


def test_setter_price(tomato):
    tomato.price = -100
    assert tomato.price == 50

    tomato.price = 0
    assert tomato.price == 50

    tomato.price = 100
    assert tomato.price == 100


def test_add_product(vegetables):
    cucumber = Product("cucumber", "It's a cucumber", 40, 1)
    vegetables.add_product(cucumber)
    assert "cucumber, 40 руб. Остаток: 1 шт." in vegetables.products
