#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10
    after asynchronously waiting for 1 second, 10 times.

    :yield: Random float number between 0 and 10
    :rtype: AsyncGenerator[float, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
