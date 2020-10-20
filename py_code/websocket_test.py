import asyncio

future = None
loop = asyncio.get_event_loop()


async def func():
    global future
    print('func begin')
    future = loop.create_future()
    ret = await future
    print('func end with %s' % ret)


async def func2():
    print('func2 begin')
    await asyncio.sleep(2)
    future.set_result('greetings from func2')
    print('func2 end')


asyncio.ensure_future(func())
asyncio.ensure_future(func2())

loop.run_forever()
loop.close()