#!/usr/bin/env python3
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def task_wait_random(max_delay: int) -> float:
    """Asynchronous function that waits for a random delay between 0 and max_delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def create_task(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for the wait_random coroutine."""
    return asyncio.create_task(task_wait_random(max_delay))