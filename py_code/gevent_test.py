import gevent
import signal
from gevent.queue import Queue as gqueue
from random import choice
from random import randint

"""
在一个线程中实现（利用gevent模块）
(1) 两个协程pinger, ponger之间通信
(2) 新建一个协程controller，可以获取pinger, ponger通信次数信息，或者控制通信的间隔
"""
class Actor(gevent.Greenlet):

    def __init__(self):
        self.inbox = gqueue()
        self.count = 0
        self.sleep_interval = 3
        gevent.Greenlet.__init__(self)

    def receive(self, message):
        raise NotImplemented()

    def _run(self):
        self.running = True
        while self.running:
            message = self.inbox.get()
            self.receive(message)


class Pinger(Actor):
    
    def receive(self, message):
        self.count += 1
        print(message + '  ' + str(self.count) + '  ' + str(self.sleep_interval))
        ponger.inbox.put('ping')
        gevent.sleep(self.sleep_interval)


class Ponger(Actor):
    def receive(self, message):
        self.count += 1
        print(message + '  ' + str(self.count) + '  ' + str(self.sleep_interval))
        pinger.inbox.put('pong')
        gevent.sleep(self.sleep_interval)


class Controller(gevent.Greenlet):

    def handler_event(self, event):
        if event['key'] == 'count': # 事件1，获取通信次数信息
            print('--count--', pinger.count, ponger.count)
        elif event['key'] == 'update_interval': # 事件2，变更通信的间隔
            print('--update interval--')
            pinger.sleep_interval = event['value']
            ponger.sleep_interval = event['value']
        else: # 事件3，其他事件
            gevent.sleep(1)
    
    def _run(self):
        self.running = True
        while self.running: # 模拟不同事件，（实际可能需要引入消息引擎，通过消费消息队列，传递不同的事件）
            events = [{'key': 'count'}, {'key': 'update_interval', 'value': randint(1, 10)}, {'key': 'others'}]
            self.handler_event(event=choice(events))
            gevent.sleep(1)

if __name__ == "__main__":

    
    pinger = Pinger()
    ponger = Ponger()
    controller = Controller()

    pinger.start()
    ponger.start()
    controller.start()

    coroutines = [pinger, ponger, controller]

    pinger.inbox.put('start')
    gevent.signal_handler(signal.SIGINT, gevent.killall, coroutines) # 发生ctrl-c信号，将所有协程kill

    try:
        gevent.joinall(coroutines)
    except Exception as e:
        print('-------This will never be reached')
