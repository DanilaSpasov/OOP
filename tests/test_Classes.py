import pytest

from src.Classes import Category, Smartphone, LawnGrass
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


def test_str_product(tomato):
    assert str(tomato) == "tomato, 50 руб. Остаток: 1 шт."


def test_str_category(vegetables, tomato):
    assert str(vegetables) == "vegetables, количество продуктов: 1 шт."


def test_add_two_products(tomato):
    cucumber = Product("cucumber", "It's a cucumber", 40, 5)
    assert tomato + cucumber == 250


def test_add_smartphones():
    samsung = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    iphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    assert samsung + iphone == 2580000


def test_add_smartphone_and_grass():
    iphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    russian_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        iphone + russian_grass


def test_add_bad_product():
    with pytest.raises(TypeError):
        Category.add_product("not a product")


def test_mixin_log(tomato):
    assert repr(tomato) == "Product(tomato,It's a tomato, 50, 1)"


def test_zero_quantity():
    with pytest.raises(ValueError):
        tomato = Product("tomato", "It's a tomato", 50, 0)


def test_middle_price(vegetables, tomato):
    cucumber = Product("cucumber", "It's a cucumber", 40, 5)
    vegetables.add_product(cucumber)
    assert vegetables.middle_price() == 45


def test_middle_price_zero_division():
    vegetables = Category("vegetables", "not fruits", [])
    assert vegetables.middle_price() == 0
