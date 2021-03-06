import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from time import sleep
'''
from matplotlib import style
style.use('fivethirtyeight')'''


#!/usr/bin/python
import os, sys
import serial


ser = serial.Serial( 'COM3' , 9600 , timeout = 10)

#position
x = []
y = []
z = []

#velocity
x_v = []
y_v = []
z_v = []


#acceleration
x_a = []
y_a = []
z_a = []



splitted_line = []


#3D
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')





'''
#2D
fig = plt.figure()
ax = plt.subplot(111)
'''

#set the limitation of the axes
ax.set_xlim(-100.00 , 100.00)
ax.set_ylim(-100.00 , 100.00)


def animate(i):
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



    splitted_line[3] = float (splitted_line[3])
    splitted_line[4] = float (splitted_line[4])
    splitted_line[5] = float (splitted_line[5])

    splitted_line[6] = float (splitted_line[6])
    splitted_line[7] = float (splitted_line[7])
    splitted_line[8] = float (splitted_line[8])



    x.append(splitted_line[0])
    y.append(splitted_line[1])
    z.append(splitted_line[2])


    x_v.append(splitted_line[3])
    y_v.append(splitted_line[4])
    z_v.append(splitted_line[5])

    x_a.append(splitted_line[6])
    y_a.append(splitted_line[7])
    z_a.append(splitted_line[8])






    ax.clear()
    ax.plot(x , y , z , 'r')
    ax.plot(x_v,  y_v, z_v , 'y')
    ax.plot(x_a, y_a, z_a, 'm')


ani = animation.FuncAnimation(fig, animate , interval=1 , repeat=True)



plt.show()