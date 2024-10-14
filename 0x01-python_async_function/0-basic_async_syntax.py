#!/usr/bin/env python3
"""Test file for  output of the wait_n coroutine"""
import asyncio
import random
"""Test file for  output of the wait_n coroutine"""

async def wait_random(max_delay: int = 10)-> int:
    """Test file rrect output of the wait_n coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
    
    
async def main():
    """Test file for printing the correc coroutine"""
    delay = await wait_random()  # Example usage with default max_delay of 10
    print(f"Waited for {delay:.2f} seconds.")

# Running the coroutine
if __name__ == "__main__":
    asyncio.run(main())