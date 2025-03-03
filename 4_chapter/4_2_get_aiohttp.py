# отправка веб-запроса с помощью aiohttp

import asyncio
from aiohttp import ClientSession
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://yandex.ru'
        status = await fetch_status(session, url)
        print(f"Состояние для {url} было равно {status}")
        
asyncio.run(main())