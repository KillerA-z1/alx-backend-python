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
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage
if __name__ == "__main__":
    # Run the coroutine and print the result
    result = asyncio.run(wait_random())
    print(f"Waited for {result:.2f} seconds")
