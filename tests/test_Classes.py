import pytest

from src.Classes import Category, Product


@pytest.fixture()
def tomato():
    return Product("tomato", "It's a tomato", 50, 1)


@pytest.fixture()
def cucumber():
    return Product("cucumber", "It's a cucumber", 30, 1)


@pytest.fixture()
def vegetables():
    return Category("vegetables", "not fruits", ["tomato", "cucumber"])


@pytest.fixture(autouse=True)
def reset_product_count():
    Product.product_count = 0


def test_init_Product(tomato):
    assert tomato.name == "tomato"
    assert tomato.description == "It's a tomato"
    assert tomato.price == 50
    assert tomato.quantity == 1


def test_init_Category(vegetables):
    assert vegetables.name == "vegetables"
    assert vegetables.description == "not fruits"
    assert vegetables.products == ["tomato", "cucumber"]


def test_product_count(tomato, cucumber):
    assert Product.product_count == 2


def test_product_count_tomato(tomato):
    assert Product.product_count == 1


def test_product_count_cucumber(cucumber):
    assert Product.product_count == 1
