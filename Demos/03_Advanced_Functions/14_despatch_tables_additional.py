# Scenario: Trade Event Processing in an OMS / Middle‑Office System
# A trading or middle‑office system might receive different kinds of events:
# - "NEW_ORDER" – a trader submits a new order
# - "CANCEL" – cancel an existing order
# - "AMEND" – modify an existing order
# - "EXECUTION" – execution report from an exchange or broker
# # Instead of using a bulky if/elif chain, a dispatch table (dictionary of functions)
# neatly routes each message type to the correct handler.

def handle_new_order(event):
    print(f"[NEW] Creating order for {event['symbol']} qty={event['qty']} at {event['price']}")

def handle_cancel(event):
    print(f"[CANCEL] Cancel order {event['order_id']}")

def handle_amend(event):
    print(f"[AMEND] Amending order {event['order_id']} with new qty={event['new_qty']}")

def handle_execution(event):
    print(f"[EXEC] Execution received: order {event['order_id']} filled {event['filled_qty']}")


# 🔥 Dispatch table maps event types → handler functions
DISPATCH_TABLE = {
    "NEW_ORDER": handle_new_order,
    "CANCEL": handle_cancel,
    "AMEND": handle_amend,
    "EXECUTION": handle_execution,
}

def process_event(event):
    event_type = event["type"]

    # Find handler, or fallback to an unknown handler
    handler = DISPATCH_TABLE.get(event_type)

    if handler:
        handler(event)
    else:
        print(f"[UNKNOWN] No handler for event type: {event_type}")

events = [
    {"type": "NEW_ORDER", "symbol": "AAPL", "qty": 100, "price": 175.5},
    {"type": "EXECUTION", "order_id": "O123", "filled_qty": 50},
    {"type": "AMEND", "order_id": "O123", "new_qty": 200},
    {"type": "CANCEL", "order_id": "O123"},
]

for e in events:
    process_event(e)


# Another Finance Example: Pricing Different Asset Types
# Many pricing systems need to call the correct model depending on the asset:
# - Equity → Black‑Scholes or dividend‑yield model
# - Bond → Discounted cash flow
# - FXOption → Garman–Kohlhagen
# - IRSwap → Curve bootstrapped valuation

def price_equity(inst):
    return inst["spot"] * inst["qty"]

def price_bond(inst):
    return inst["face"] * inst["price"] / 100

def price_fx_option(inst):
    return "Using FX option model..."

def price_swap(inst):
    return "Using swap curve pricing..."


PRICE_DISPATCH = {
    "Equity": price_equity,
    "Bond": price_bond,
    "FXOption": price_fx_option,
    "IRSwap": price_swap,
}

def price_instrument(inst):
    model = PRICE_DISPATCH.get(inst["type"])
    if not model:
        raise ValueError("Unknown instrument type")
    return model(inst)


instruments = [
    {"type": "Equity", "equity_id": "AAPL", "spot": 100, "qty": 20},
    {"type": "Bond", "bond_id": "O123", "face": 50, "price": 200.00},
    {"type": "FXOption", "order_id": "O123", "new_qty": 200},
    {"type": "IRSwap", "order_id": "O123"},
]

for inst in instruments:
    print(price_instrument(inst))