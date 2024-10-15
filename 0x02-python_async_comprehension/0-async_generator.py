#!/usr/bin/env python3
"""
This module contains an asynchronous generator function.

Functions:
    async_generator: Asynchronously generates 10 random float numbers
    between 0 and 10,with a 1-second delay between each number.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Loop 10 times, each time asynchronously wait 1 second,
        then yield a random number between 0 and 10.'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
