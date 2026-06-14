import pytest

from src.Classes import Category, Product


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
    assert vegetables.products == [tomato]


def test_category_count(tomato, vegetables):
    assert Category.product_count == 1
    assert Category.category_count == 1


