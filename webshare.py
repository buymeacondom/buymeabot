import random


async def fetch(limit: int = 10) -> list[str]:
    """Free proxy fetcher stub."""
    return [f"http://user{random.randint(1,999)}:pass{random.randint(1000,9999)}@127.0.0.{random.randint(1,255)}:{random.randint(10000,65535)}" for _ in range(limit)]
