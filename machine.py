import tkinter as tk

root = tk.Tk()
root.title("Circular NeoPixel Simulation")

class Timer:
    PERIODIC = 1
    def __init__(self, i):
        pass

    def init(self, period, mode, callback):
        print(f"period is {period}")
        callback(1)
        root.after(period, lambda: self.init(period, mode, callback))


def Pin(a):
    pass