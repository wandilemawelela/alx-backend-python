#!/usr/bin/env python3
import asyncio
import time
from typing import List
from wait_n import wait_n  # Import wait_n from the previous file


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) 
    nd returns the average time per call.
    
    :param n: Number of times to spawn wait_random
    :type n: int
    :param max_delay: Maximum delay in seconds for wait_random
    :type max_delay: int
    :return: Average time per call
    :rtype: float
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
