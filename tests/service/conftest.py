import pytest
from src import database
from src.daos.base_dao import BaseDao
# Mock Database Singleton connection


@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    def mock(*args, **kwargs):
        pass
    monkeypatch.setattr(database.Database, '__init__', mock)
    monkeypatch.setattr(database.Database, 'to_dict', mock)


@pytest.fixture(autouse=True)
def mock_base_dao(monkeypatch):
    def mock(*args,  **kwargs):
        pass
    monkeypatch.setattr(BaseDao, '__enter__', mock)
    monkeypatch.setattr(BaseDao, '__exit__', mock)
    monkeypatch.setattr(BaseDao, 'session', mock)
