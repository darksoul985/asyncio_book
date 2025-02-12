import asyncio
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed, delay

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter += 1
        
    return counter

@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    
    await task_one
    await task_two
    
asyncio.run(main())