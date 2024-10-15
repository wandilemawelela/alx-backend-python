import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay (inclusive)
    and returns the delay.

    :param max_delay: Maximum delay in seconds,
    defaults to 10
    :type max_delay: int, optional
    :return: The actual delay in seconds
    :rtype: float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
