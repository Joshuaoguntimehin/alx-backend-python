#!/usr/bin/env python3
"""import statement"""
import asyncio
import asyncio
"""import statement"""

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measure total runtime of  4 times in parallel."""
    start_time = asyncio.get_event_loop().time()  # Record start time

    # Run async_comprehension 4 times concurrently using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = asyncio.get_event_loop().time()  # Record end time

    # Calculate and return total runtime
    return end_time - start_time
z