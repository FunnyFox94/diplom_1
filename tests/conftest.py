import pytest

from src.bun import Bun
from src.burger import Burger
from src.database import Database
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def create_database():
    return Database


@pytest.fixture
def black_bun():
    return Bun("black bun", 100)


@pytest.fixture
def hot_sauce_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)


@pytest.fixture
def sour_cream_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)


@pytest.fixture
def burger():
    return Burger()
