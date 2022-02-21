import matplotlib.animation as anm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10, 6))
x = np.arange(0, 10, 0.1)

def update(i, fig_title, A):
    if i != 0:
        plt.cla()

    y = A * np.sin(x - i)
    plt.plot(x, y, "r")
    plt.title(fig_title + '=' + str(i) + 'ms')


ani = anm.FuncAnimation(fig, update, fargs = ('Elapsed time ', 2.0), \
    interval = 100, frames = 132)

ani.save("Sample.gif", writer = 'imagemagick')