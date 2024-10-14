#!/usr/bin/env python3
"""Test file for  output of the wait_n coroutine"""
import asyncio
import random
'''Test file for  output of the wait_n coroutine'''
async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that waits for a random delay and returns it.'''
    delay = random.uniform(0, max_delay)  
    '''Generate a random float between 0 and max_delay'''
    await asyncio.sleep(delay)  # Wait asynchronously for the delay
    return delay
