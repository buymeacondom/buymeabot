import random
import asyncio


async def check(cc: str, proxy: dict | None = None) -> dict:
    """B3 Auth gate stub."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "approved", "code": "LIVE", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "amount": "$0.00"},
    ]
    weights = [20, 60, 20]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "B3_AUTH", "cc": cc, "site": "b3gateway.com", **result}
