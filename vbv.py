import random
import asyncio


async def check(cc: str, proxy: dict | None = None) -> dict:
    """Braintree VBV gate stub."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "3ds", "code": "3DS_REQUIRED", "amount": "$0.00"},
        {"status": "approved", "code": "LIVE", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "amount": "$0.00"},
    ]
    weights = [20, 15, 45, 20]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "BRAINTREE_VBV", "cc": cc, "site": "braintree.com", **result}
