import random
import asyncio


async def check_card_site(cc: str, proxy: dict | None = None, site: str | None = None) -> dict:
    """Shopify gate stub. Returns a realistic check response."""
    await asyncio.sleep(random.uniform(0.8, 2.0))
    outcomes = [
        {"status": "charged", "code": "ORDER_PLACED", "site": site or "shop.myshopify.com", "amount": "$5.00"},
        {"status": "approved", "code": "LIVE", "site": site or "shop.myshopify.com", "amount": "$0.00"},
        {"status": "approved", "code": "INSUFFICIENT_FUNDS", "site": site or "shop.myshopify.com", "amount": "$0.00"},
        {"status": "declined", "code": "DECLINED", "site": site or "shop.myshopify.com", "amount": "$0.00"},
        {"status": "dead", "code": "DEAD", "site": site or "shop.myshopify.com", "amount": "$0.00"},
    ]
    weights = [2, 8, 12, 60, 18]
    result = random.choices(outcomes, weights=weights, k=1)[0]
    return {
        "gate": "SHOPIFY",
        "cc": cc,
        "proxy": proxy.get("host") if proxy else None,
        **result,
    }
