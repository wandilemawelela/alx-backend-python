#!/usr/bin/env python3

import asyncio
import random
import time
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


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    :return: Total runtime in seconds
    :rtype: float
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
