import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def create_database():
    return Database


@pytest.fixture
def black_bun():
    return Bun("black bun", 100)


@pytest.fixture
def hot_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)


@pytest.fixture
def sour_cream():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)


@pytest.fixture
def burger():
    return Burger()
