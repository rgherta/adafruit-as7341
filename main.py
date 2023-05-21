# BLINKA_MCP2221=1 python3 main.py

import board

from adafruit_as7341 import AS7341

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = AS7341(i2c)


fig, ax = plt.subplots()
x = [415, 445, 480, 515, 555, 590, 630, 680]
y = [0,0,0,0,0,0,0,0]
ax.plot(x, y)


def update(frame):

    global x, y
    ax.clear()
    y = sensor.all_channels
    ax.plot(x, y)
    ax.grid()



animation = FuncAnimation(fig, update, interval=1000, repeat = True)
plt.show()
    