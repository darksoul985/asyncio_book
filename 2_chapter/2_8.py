import asyncio
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)

asyncio.run(main())