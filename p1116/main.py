from multiprocessing import Queue
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 1
        self.qzero = Queue(1)
        self.qodd = Queue(1)
        self.qeven = Queue(1)
        self.qzero.put(0)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            # print('debug:', self.i)
            self.qzero.get()
            # print('debug: got', self.i)
            printNumber(0)
            if self.i % 2 == 1:
                self.qodd.put(self.i)
            else:
                self.qeven.put(self.i)
            self.i += 1
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        if self.n < 2:
            return
        while True:
            # print('debug: even')
            ii = self.qeven.get()
            # print('debug: got even')
            printNumber(ii)
            if ii <= self.n-1:
                self.qzero.put(0)
            if ii >= self.n-1:
                break 
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            # print('debug: odd')
            ii = self.qodd.get()
            # print('debug: got odd')
            printNumber(ii)
            if ii <= self.n-1:
                self.qzero.put(0)
            if ii >= self.n-1:
                break 

obj  = ZeroEvenOdd(10)
t1 = threading.Thread(target=obj.zero, args=(print,))
t2 = threading.Thread(target=obj.even, args=(print,))
t3 = threading.Thread(target=obj.odd, args=(print,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()