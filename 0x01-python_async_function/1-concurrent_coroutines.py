#!/usr/bin/env python3
"""
This module contains two asynchronous functions: wait_random and wait_n.
Functions:
    wait_random(max_delay: int = 10) -> float:
        Wait up to max_delay seconds and then return the length of the delay.
    wait_n(n: int, max_delay: int) -> List[float]:
        Spawn wait_random n times with the specified max_delay and return the
        list of delays in ascending order.
"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay seconds then return the length of the delay.'''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Spawn wait_random n times with the specified max_delay and return the
    list of delays in ascending order. '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Manually sort the delays
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
