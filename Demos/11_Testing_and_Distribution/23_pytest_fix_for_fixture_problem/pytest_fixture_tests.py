import pytest

@pytest.fixture
def db():
    return "database connection"

@pytest.fixture
def api_client():
    return "API client"

def test_db_operation(db):
    assert db == "database connection"

def test_api_call(api_client):
    assert api_client == "API client"

