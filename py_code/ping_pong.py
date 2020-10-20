import asyncio

ping_count = 0
pong_count = 0

class Actor(object):

    def __init__(self):
        self.inbox = asyncio.Queue()

    def send(self, message):
        self.inbox.put_nowait(message)

    async def receive(self, message):
        raise NotImplemented()

    async def run(self):
        self.running = True
        while self.running:
            message = await self.inbox.get()
            await self.receive(message)


class Pinger(Actor):

    async def receive(self, message):
        global ping_count
        print(message)
        pong.send('ping' + str(ping_count))
        ping_count += 1
        await asyncio.sleep(3)


class Ponger(Actor):

    async def receive(self, message):
        global pong_count
        print(message)
        ping.send('pong' + str(pong_count))
        pong_count += 1
        await asyncio.sleep(3)

class Listener():

    async def handler_event(self, event):
        if event == 'count_message':
            print(ping_count, pong_count)
        elif event == 'update_timeout':
            pass

    async def run(self):
        while True:
            await asyncio.sleep(10)
            await self.handler_event(event='count_message')


def start():

    ping = Pinger()
    pong = Ponger()
    # listener = Listener()

    ping.send('start')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait(
            (
                ping.run(), 
                pong.run()
            )
        )
    )
    loop.close()


if __name__ == "__main__":
    print('--start--')
    start()
    print('--end--')