import asyncio
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed

@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'Засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течении {delay_seconds} с закончился')

@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    
    await task_one
    await task_two
    
asyncio.run(main())