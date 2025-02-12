import asyncio
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import delay


async def main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)

    except TimeoutError:
        print("Задача заняла более 5 с, скоро она закончиться!")
        result = await task
        print(result)

asyncio.run(main())