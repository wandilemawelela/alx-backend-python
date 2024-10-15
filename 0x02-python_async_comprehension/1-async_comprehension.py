#!/usr/bin/env python3

import asyncio
import random
from typing import List, AsyncGenerator


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


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an asynchronous comprehension and returns them.

    :return: List of 10 random float numbers
    :rtype: List[float]
    """
    return [number async for number in async_generator()]
