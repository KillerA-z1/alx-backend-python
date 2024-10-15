#!/usr/bin/env python3
"""
This module provides a coroutine to collect random numbers
using async comprehension.

Functions:
    async_comprehension() -> List[float]: Collects 10 random numbers using
    an async comprehension over async_generator.
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collects 10 random numbers using an async comprehension over
    async_generator.'''
    return [number async for number in async_generator()]
