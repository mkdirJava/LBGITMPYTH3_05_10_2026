import asyncio

from behave import given, when, then
from httpx import AsyncClient


async def make_request(context, method, url, **kwargs):

    async with AsyncClient(
        transport=context.transport,
        base_url="http://test"
    ) as client:

        return await client.request(
            method,
            url,
            **kwargs
        )


@given("a registered customer")
def step_registered_customer(context):
    context.username = "alice"
    context.password = "password123"


@when("they login with valid credentials")
def step_login(context):

    response = asyncio.run(
        make_request(
            context,
            "POST",
            "/accounts/login",
            json={
                "username": context.username,
                "password": context.password,
            },
        )
    )

    context.token = response.json()["access_token"]


@when("they request their account details")
def step_get_account(context):

    context.response = asyncio.run(
        make_request(
            context,
            "GET",
            "/accounts/accounts/me",
            headers={
                "Authorization":
                    f"Bearer {context.token}"
            },
        )
    )


@then("the request should succeed")
def step_success(context):
    assert context.response.status_code == 200

@then("the account balance should be returned")
def step_balance_returned(context):
    data = context.response.json()
    assert data["account_id"] == "ACC-001"
    assert data["currency"] == "GBP"
    assert data["balance"] == 12500.75