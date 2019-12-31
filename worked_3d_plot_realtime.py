import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#!/usr/bin/python
import os, sys
import serial

ser = serial.Serial( 'COM3',9600, timeout = 0.5)


x = []
y = []
z = []


splitted_line = []

fig = plt.figure()
ax1 = Axes3D(fig)

ax1.set_xlim3d(-1000, 1000)
ax1.set_ylim3d(-1000,1000)
ax1.set_zlim3d(-1000,1000)
'''
fig = plt.figure()
ax1 = fig.add_subplot(19,8,2)
ax2 = fig.add_subplot(14,8,4)'''

'''
x = [54 , 65 ,64 , 23 ,33.5 , -76.65]
y = [3 , 54 ,2 ,2 , -0.532 , -.54 ]
z = [34 , 54 ,6 , 1 , 4 , -43]
'''
x = []
y = []
z = []

def animate(i):
    ax1.set_xlim3d(-1000.00, 1000.00)
    ax1.set_ylim3d(-1000.00, 1000.00)
    ax1.set_zlim3d(-1000.00, 1000.00)
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

    ax1.clear()
    ax1.plot3D(x , y , z)


ani = animation.FuncAnimation(fig, animate, interval=100 , repeat=True)
plt.show()