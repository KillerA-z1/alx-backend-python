#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of executing
multiple coroutines.
Functions:
    measure_time(n: int, max_delay: int) -> float:
        Measures the total execution time for wait_n(n, max_delay) and returns
        the average time per coroutine.
"""
from time import perf_counter
from asyncio import run
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine. '''
    start_time = perf_counter()
    run(wait_n(n, max_delay))
    end_time = perf_counter()

    total_time = end_time - start_time
    return total_time / n
