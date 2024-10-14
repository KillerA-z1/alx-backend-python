#!/usr/bin/env python3
"""
This module contains an asynchronous function that waits for a random delay.

Functions:
    wait_random(max_delay: int = 10) -> float:
        Asynchronously waits for a random delay between 0 and max_delay seconds
        and returns the actual delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay.

    This function generates a random delay between 0 and `max_delay` seconds,
    then asynchronously waits for that delay before returning the actual delay.

    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
