from multiprocessing import Queue
class Foo:
    ''' 
    用队列和监听来控制时序
    '''
    pw = None
    pr = None
    q = None
    

    def __init__(self):
        # 父进程创建Queue，并传给各个子进程：
        self.q = Queue()

    

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.q.put(1)


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        while True:
            value = self.q.get()
            if value == 1:
                break
            else:
                self.q.put(value)
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.q.put(2)


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        while True:
            value = self.q.get()
            if value == 2:
                break
            else:
                self.q.put(value)
        # printThird() outputs "third". Do not change or remove this line.
        printThird()



