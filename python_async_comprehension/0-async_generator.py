#!/usr/bin/env python3
"""Module for async generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random floats between 0 and 10, waiting 1 second each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
