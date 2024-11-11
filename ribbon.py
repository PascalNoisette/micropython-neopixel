import machine, neopixel
from machine import Timer

BLUE_LED_PIN = 8

class Ribbon:
    """The controls to allow you to vary the rainbow and blink animations."""
    def __init__(self):
        self.reverse = False
        self.num_pixels = 60 # 3m - SMD5050, group of 3 led per WS2811, 60Leds/m . The LEDs basically have a WS2811 inside, but fixed at the 800KHz 'high speed' setting. Our wonderfully-written Neopixel library for Arduino supports these pixels! As it requires hand-tuned assembly it is only for AVR cores but others may have ported this chip driver code so please google around. An 8MHz or faster processor is required.
        self.data_pin = 6
        self.wait = 0.0
        self.speed=20 # led_as_lenght_unit per second
        self.fps = 10 # should be equal or faster than led to avoid skiping any led in between exept to preserve cpu
        self.elapsed = self.generate()
        self.elapsedMs = 0
        self.timer = Timer(-1)
        self.np = neopixel.NeoPixel(machine.Pin(self.data_pin), self.num_pixels)

    def generate(self):
        while True:
            self.elapsedMs = self.elapsedMs + int(1000/self.fps)
            yield int(self.elapsedMs)

    def stop_animation(self):
        self.timer.deinit()
        self.elapsedMs = 0

    def reset(self):
        machine.reset()

    def start_animation(self, callback):
        self.timer.init(period=int(1000/self.fps), mode=Timer.PERIODIC, callback=lambda t: callback(self.np, self.num_pixels, next(self.elapsed), self.speed))

    def display(self, callback):
        callback(self.np, self.num_pixels, next(self.elapsed), self.speed)

