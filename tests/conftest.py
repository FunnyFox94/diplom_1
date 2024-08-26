import pytest

from praktikum.database import Database


@pytest.fixture
def create_database():
    return Database