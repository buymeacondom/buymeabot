import random


async def scrape(query: str, limit: int = 20) -> list[str]:
    """Brave URL scraper stub."""
    return [f"https://example-site-{i}.com" for i in range(min(limit, 20))]
