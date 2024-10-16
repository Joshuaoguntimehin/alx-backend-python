#!/usr/bin/env python3
"""Test file for printing the correct output of the wait_n coroutine"""
import asyncio
import random
import heapq
"""Asynchronous function that waits for a random delay between 0 and max_delay."""
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    """Asynchronous function that waits for a random delay between 0 and max_delay."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)
    
    return delays