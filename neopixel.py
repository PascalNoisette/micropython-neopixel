
import tkinter as tk
from machine import root
import math

class NeoPixel(object):
    def __init__(self, pin, pixels):
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.num_pixels = pixels
        self.radius = 150
        self.center_x = 200  # Center of the circle (x)
        self.center_y = 200  # Center of the circle (y)
        self.squares = []
        self.colors = [(0, 0, 0)] * pixels  # Initialize all pixels as 'off' (black)
        self.angle_step = 360 / pixels  # Angle between each pixel

        # Create the pixels (circles) in a circular pattern
        for i in range(pixels):
            angle = math.radians(i * self.angle_step)
            x0 = self.center_x + self.radius * math.cos(angle) - 15
            y0 = self.center_y + self.radius * math.sin(angle) - 15
            x1 = x0 + 30
            y1 = y0 + 30
            circle = self.canvas.create_oval(x0, y0, x1, y1, outline="black", fill='black')
            self.squares.append(circle)

    def __setitem__(self, index, color):
        """Simulates setting a pixel color via (R, G, B) tuple"""
        self.colors[index] = color
        hex_color = self.rgb_to_hex(color)
        self.canvas.itemconfig(self.squares[index], fill=hex_color)


    def rgb_to_hex(self, rgb):
        """Convert (R, G, B) tuple to hex color for tkinter"""
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    def __getitem__(self, key):
        return self.colors[key]
    
    def write(self):
        pass

    def fill(self, c):
        for i in range(self.num_pixels):
            self[i] = c