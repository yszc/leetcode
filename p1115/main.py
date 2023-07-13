from multiprocessing import Queue

class FooBar:
    def __init__(self, n):
        self.n = n
        self.q = Queue()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.q.put(1)
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.q.get()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()