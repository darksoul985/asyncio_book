from aiohttp import ClientSession
import asyncio
import random
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # await asyncio.sleep(random.randint(2, 4))
    async with session.get(url) as result:
        return result.status