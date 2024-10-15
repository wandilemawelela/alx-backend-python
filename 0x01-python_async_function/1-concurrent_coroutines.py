#!/usr/bin/env python3
"""
The following module imports wait_random from the previous
python file and uses an async routine called wait_n that
takes in 2 int arguments (in this order): n and max_delay.
"""

import asyncio
import random
import heapq
from typing import List


# Assuming wait_random is in the same file for simplicity
# If it's in a different file, you would use: from <module>
# import wait_random
async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    :param n: Number of times to spawn wait_random
    :type n: int
    :param max_delay: Maximum delay in seconds for wait_random
    :type max_delay: int
    :return: List of delays in ascending order
    :rtype: List[float]
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)

    return [heapq.heappop(delays) for _ in range(n)]
