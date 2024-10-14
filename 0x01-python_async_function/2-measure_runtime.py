#!/usr/bin/env python3
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start =  time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    print(f'Task completed in {end - start:.2f} seconds.')
    
    total_time = end - start
    return total_time / n
    