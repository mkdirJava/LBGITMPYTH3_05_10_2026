import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_get_account_authenticated():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        # Login and obtain JWT
        login_response = await client.post(
            "/accounts/login",
            json={
                "username": "alice",
                "password": "password123"
            }
        )

        assert login_response.status_code == 200

        token = login_response.json()["access_token"]

        # Use JWT to call protected endpoint
        account_response = await client.get(
            "accounts/accounts/me",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

    assert account_response.status_code == 200

    data = account_response.json()

    assert data["account_id"] == "ACC-001"
    assert data["balance"] == 12500.75
    assert data["currency"] == "GBP"


@pytest.mark.asyncio
async def test_login_with_invalid_credentials():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.post(
            "/accounts/login",
            json={
                "username": "alice",
                "password": "wrong-password"
            }
        )

    assert response.status_code == 401



@pytest.mark.asyncio
async def test_get_account_without_token():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.get("/accounts/accounts/me")

    assert response.status_code in (401, 403)


@pytest.mark.asyncio
async def test_get_account_with_invalid_token():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:

        response = await client.get(
            "/accounts/accounts/me",
            headers={
                "Authorization": "Bearer invalid-token"
            }
        )

    assert response.status_code == 401