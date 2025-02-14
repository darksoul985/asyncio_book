# Неправильное использование спискового включения
# для создания и ожидания задач
import asyncio
import sys
sys.path.append(r'C:\Users\shirobokovsv1\Documents\project\Asincio_book')
from util import async_timed, delay

@async_timed()
async def main() -> None:
    delay_times = [3, 4, 5]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())