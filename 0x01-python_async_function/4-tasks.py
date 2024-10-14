#!/usr/bin/env python3
"""
This module provides a function to create multiple asyncio.Tasks for
the wait_random function.

Functions:
    task_wait_n(n: int, max_delay: int) -> List[float]:
        Spawns n tasks using task_wait_random and returns the list of all
        delays (float values).
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Spawns n tasks using task_wait_random and returns the list of all
    delays (float values).'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
