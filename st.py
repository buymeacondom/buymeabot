import random
import asyncio


async def check(cc: str, proxy: dict | None = None, site: str | None = None) -> dict:
    """WooCommerce ST gate stub."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "charged", "code": "ORDER_PLACED", "site": site or "woocommerce-store.com", "amount": "$5.00"},
        {"status": "approved", "code": "LIVE", "site": site or "woocommerce-store.com", "amount": "$0.00"},
        {"status": "approved", "code": "INSUFFICIENT_FUNDS", "site": site or "woocommerce-store.com", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "site": site or "woocommerce-store.com", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "site": site or "woocommerce-store.com", "amount": "$0.00"},
    ]
    weights = [2, 8, 12, 60, 18]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {"gate": "WOOCOMMERCE_ST", "cc": cc, **result}
