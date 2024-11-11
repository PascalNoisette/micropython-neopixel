import tkinter as tk

root = tk.Tk()
root.title("Circular NeoPixel Simulation")

class Timer:
    PERIODIC = 1
    def __init__(self, i):
        pass

    def init(self, period, mode, callback):
        callback(1)
        root.after(100, lambda: self.init(period, mode, callback))


def Pin(a):
    pass