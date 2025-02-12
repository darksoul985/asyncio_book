import asyncio

async def delay(delay_seconds: int) -> int:
    print(f'засыпю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон на {delay_seconds} с закончился')
    return delay_seconds