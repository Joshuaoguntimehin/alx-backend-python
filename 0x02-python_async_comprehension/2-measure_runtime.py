#!/usr/bin/env python3
"""import statement"""
import asyncio
import random
import time 
"""import statement"""
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_runtime = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    total_time = time.perf_counter()
    return total_time
#print(f'Total runtime: {total_time:.2f} seconds')