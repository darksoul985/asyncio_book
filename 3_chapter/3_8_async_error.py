import asyncio
import socket
from asyncio import AbstractEventLoop
import logging

async def listen_for_connections(server_socket: socket,
                                 loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение: {address}")
        asyncio.create_task(echo(connection, loop))

async def echo(connection: socket,
               loop: AbstractEventLoop) ->None:
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b'boom\r\n':
                raise Exception("Неожиданная ошибка сети")

            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(ex)

    finally:
        connection.close()

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = ('127.0.0.1', 8888)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())