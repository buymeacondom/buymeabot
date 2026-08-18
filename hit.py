import random
import asyncio


async def check(cc: str, proxy: dict | None = None) -> dict:
    """Stripe Checkout HIT gate stub."""
    await asyncio.sleep(random.uniform(1.0, 3.0))
    outcomes = [
        {"status": "charged", "code": "ORDER_PLACED", "amount": "$5.00"},
        {"status": "approved", "code": "LIVE", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "amount": "$0.00"},
    ]
    weights = [3, 12, 60, 25]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "STRIPE_CHECKOUT", "cc": cc, "site": "checkout.stripe.com", **result}
