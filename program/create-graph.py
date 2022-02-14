import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/gaze.csv').values.tolist()

def setBackgroundColor():
    fig = plt.figure()
    ax = fig.add_subplot(211)
    fig.patch.set_facecolor('#FFF')
    ax.patch.set_facecolor('#00FF00')

def displayCoordinateGraph(x,y):
    # setBackgroundColor()
    plt.title('Gaze of a PC screen(From Bereaved family)')
    plt.xlim([0,3840])
    plt.ylim([0,2160])
    plt.scatter(x,y,c='pink',marker='.')
    # plt.colorbar()
    plt.show()

def createScatterDiagram():
    x = []
    y = []
    for coord in data:
        x.append(coord[0])
        y.append(coord[1])
    displayCoordinateGraph(x,y)

createScatterDiagram()