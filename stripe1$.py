import random
import asyncio


async def check(cc: str, proxy: dict | None = None) -> dict:
    """Stripe $1 gate stub."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "charged", "code": "ORDER_PLACED", "amount": "$1.00"},
        {"status": "approved", "code": "LIVE", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "amount": "$0.00"},
    ]
    weights = [5, 15, 55, 25]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "STRIPE_1DOLLAR", "cc": cc, "site": "stripe.com", **result}
