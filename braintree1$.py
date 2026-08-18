import random
import asyncio


async def check(cc: str, proxy: dict | None = None) -> dict:
    """Braintree Auth gate stub."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "approved", "code": "LIVE", "amount": "$0.00"},
        {"status": "approved", "code": "INSUFFICIENT_FUNDS", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "amount": "$0.00"},
    ]
    weights = [15, 15, 50, 20]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "BRAINTREE_AUTH", "cc": cc, "site": "braintree.com", **result}
