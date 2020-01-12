'''

reads data from usb port and plot them frame is updated every 1
miliseconds while usb port sends each packets of data (144bits) in 144/9600 seconds
meaning each seconds sends about 66 packets of data

'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import style
style.use('fivethirtyeight')


#!/usr/bin/python
import os, sys
import serial

ser = serial.Serial( 'COM3',9600, timeout = 10)


x = []
y = []
z = []


splitted_line = []

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

def animate(i):
    '''
    ax1.set_xlim3d(-1000.00, 1000.00)
    ax1.set_ylim3d(-1000.00, 1000.00)
    ax1.set_zlim3d(-1000.00, 1000.00)'''
    print (i)
    lines = ser.readline()
    print(lines)
    if len(lines) == 0:
        print("Time out! Exit.\n")
        sys.exit()

    str_line = lines.decode('unicode_escape')
    splitted_line = str_line.split()

    #print(splitted_line[0] ,splitted_line[1] , splitted_line[2])

    splitted_line[0] = float (splitted_line[0])
    splitted_line[1] = float (splitted_line[1])
    splitted_line[2] = float (splitted_line[2])

    #print("dis")
    '''
    x = list(map(float, x))
    y = list(map(float, y))
    z = list(map(float, z))'''



    x.append(splitted_line[0])
    y.append(splitted_line[1])
    z.append(splitted_line[2])


    print(x[i])
    print(y[i])
    print(z[i])
    print(i)
    ax1.clear()
    ax1.plot(x , y , z)



ani = animation.FuncAnimation(fig, animate , interval=1 , repeat=True)
plt.show()