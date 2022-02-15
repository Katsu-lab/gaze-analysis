import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

data = pd.read_csv('../data/gaze.csv').values.tolist()

def displayCoordinateGraph(x,y):
    fig = plt.figure()
    ax1 = fig.add_subplot()
    fig.patch.set_facecolor('#FFF')
    ax1.patch.set_facecolor('#00FF00')
    line = ax1.scatter(x,y,c='red',marker='.')
    plt.title('Gaze of a PC screen(From Bereaved family)')
    plt.xlim([0,3840])
    plt.ylim([0,2160])
    plt.show()
    # plt.colorbar()

def createScatterDiagram():
    x = []
    y = []
    for coord in data:
        x.append(coord[0])
        y.append(coord[1])
    displayCoordinateGraph(x,y)

createScatterDiagram()