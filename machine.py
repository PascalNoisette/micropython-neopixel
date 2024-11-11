import datetime, threading

class Timer:
    PERIODIC = 1
    def __init__(self, i):
        pass
    def init(self, period, mode, callback):
        callback(1)
        threading.Timer(period/1000, lambda:  self.init(period, mode, callback)).start()

    
def Pin(a):
    pass