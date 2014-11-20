import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def solveCase2(dt=1/100., t_max=10000, x_i=1.7, y_i=1.7, z_i=1.7,
               x_c=1, a=1, b=1, c=1, d=1, e=1, f=1, g=1):
    t = 0.
    x = x_i
    y = y_i
    z = z_i
    x_list = [x]
    y_list = [y]
    z_list = [z]
    c_list = [t]
    while t < t_max:
        dx = a*x - b*(x/x_c - 1)*x*y
        dy = -c*y + d*(x/x_c - 1)*x*y + e*(2 - x/x_c)*y*z
        dz = f*z + - g*(2 - x/x_c)*z*y
        x = x + dt*dx
        y = y + dt*dy
        z = z + dt*dz
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        c_list.append(t)
        t = t+dt
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_list, y_list, z_list, c=c_list)
    plt.show()


def timeCase2(dt=1/10., t_max=1000, x_i=1.7, y_i=1.7, z_i=1.7,
              x_c=1, a=1, b=1, c=1, d=1, e=1, f=1, g=1):
    plt.ion()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim(1,2)
    ax.set_ylim(0,5)
    ax.set_zlim(0,2)
    plt.show()
    t = 0.
    x = x_i
    y = y_i
    z = z_i
    x_list = [x]
    y_list = [y]
    z_list = [z]
    c_list = [t]
    while t < t_max:
        dx = a*x - b*(x/x_c - 1)*x*y
        dy = -c*y + d*(x/x_c - 1)*x*y + e*(2 - x/x_c)*y*z
        dz = f*z + - g*(2 - x/x_c)*z*y
        x = (x + dt*dx) if x>0 else 0
        y = (y + dt*dy) if y>0 else 0
        z = (z + dt*dz) if z>0 else 0
        x_list.append(x)
        y_list.append(y)
        z_list.append(z)
        c_list.append(t)
        t = t+dt
        ax.scatter(x,y,z)
        plt.draw()
