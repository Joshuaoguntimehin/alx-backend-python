#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10)-> int:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
    
    
async def main():
    delay = await wait_random()  # Example usage with default max_delay of 10
    print(f"Waited for {delay:.2f} seconds.")

# Running the coroutine
if __name__ == "__main__":
    asyncio.run(main())