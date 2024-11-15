from rainbowio import colorwheel
import math

def clean(np, num_pixels, time, speed):
    np.fill((0, 0, 0))
    np.write()


def white(np, num_pixels, time, speed):
    np.fill((255, 255, 255))
    np.write()


def red(np, num_pixels, time, speed):
    np.fill((255, 0, 0))
    np.write()



def change_color(np, num_pixels, time, speed):
    for i in range(num_pixels):
        rc_index = (i * 256 // num_pixels) + (int(time / 1000 * speed) % 255)
        np[i] = colorwheel(rc_index & 255)
    np.write()


def cycle(np, num_pixels, time, speed):
    np.fill((0, 0, 0))
    np[int(time / 1000 * speed) % num_pixels] = (255, 255, 255)
    np.write()
