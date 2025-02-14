import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed

@async_timed()
async def fetch_status(session: ClientSession,
                       url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=.6)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status
    
@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with ClientSession(timeout=session_timeout) as session:
        status = await fetch_status(session, 'https://google.com')
        print(f"Состояние для было равно {status}")

asyncio.run(main())