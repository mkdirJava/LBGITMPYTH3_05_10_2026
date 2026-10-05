import pytest
from aiohttp import web

# Import your app and handler
from bankserver import create_app # change to actual module name

# aiohttp test client fixture
@pytest.fixture
async def client(aiohttp_client):
    app = create_app()  # NEW instance per test
    return await aiohttp_client(app)

# Test: valid account
async def test_get_balance_success(client):
    resp = await client.post("/balance", json={"account_id": "A100"})

    assert resp.status == 200
    data = await resp.json()

    assert data["status"] == "success"
    assert data["account"] == "A100"
    assert data["balance"] == 500

# Test: another valid account
async def test_get_balance_another_account(client):
    resp = await client.post("/balance", json={"account_id": "B200"})

    assert resp.status == 200
    data = await resp.json()

    assert data["status"] == "success"
    assert data["balance"] == 300

# Test: invalid account
async def test_get_balance_not_found(client):
    resp = await client.post("/balance", json={"account_id": "X999"})

    assert resp.status == 404
    data = await resp.json()

    assert data["status"] == "error"
    assert data["message"] == "Account not found"

# Test: missing account_id field
async def test_get_balance_missing_field(client):
    resp = await client.post("/balance", json={})

    assert resp.status == 404  # current implementation treats None as not found
    data = await resp.json()

    assert data["status"] == "error"
    assert data["message"] == "Account not found"