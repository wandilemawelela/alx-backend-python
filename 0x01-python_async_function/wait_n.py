#!/usr/bin/env python3

import asyncio
from typing import List
from 1-wait_random import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays
