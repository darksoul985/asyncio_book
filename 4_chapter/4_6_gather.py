# Конкурентное выполнение запросов с помощью gather

import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import fetch_status, async_timed, urls


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        # status_codes = [await fetch_status(session, url) for url in urls]
        for i in status_codes:
            print(i)
        
asyncio.run(main())