#!/usr/bin/env python3
import asyncio
import random
"""import statement"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    random_number = [num async for num in async_generator()]
    return random_number
