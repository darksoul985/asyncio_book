import asyncio, signal
from asyncio import AbstractEventLoop
from typing import Set
import sys
sys.path.append(r'/mnt/c/Users/shirobokovsv1/Documents/project/Asincio_book')

from util import delay

def cancel_tasks():
    print('Получен сигнал SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Снимается {len(tasks)} задач.')
    [task.cancel() for task in tasks]

async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    await delay(10)

asyncio.run(main())