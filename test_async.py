import asyncio

async def tcp_echo(message:str) -> None:
    reader, writer = await asyncio.open_connection('localhost', 6969)
    print('sending message')
    writer.write(message.encode())
    data = await reader.read(100)
    print( f'received: {data.decode()}')
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_echo('Hello World!'))