from aiohttp import web

ACCOUNTS = {"A100": 500, "B200": 300, "C300": 900,}

async def get_balance(request):
    data = await request.json()
    account_id = data.get("account_id")

    print(f"Request for account {account_id}")

    balance = ACCOUNTS.get(account_id)

    if balance is None:
        return web.json_response(
            {"status": "error", "message": "Account not found"},
            status=404
        )

    return web.json_response(
        {"status": "success", "account": account_id, "balance": balance}
    )

app = web.Application()
app.router.add_post("/balance", get_balance)

# Run server:
web.run_app(app, host="127.0.0.1", port=8080)