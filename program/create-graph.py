import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/gaze.csv').values.tolist()

def displayCoordinateGraph(x,y):
    plt.xlim([0,3840])
    plt.ylim([0,2160])
    plt.scatter(x,y,c="b",marker=".",alpha=0.5)
    plt.title('Gaze of a PC screen(From Bereaved family)')
    plt.show()

def createScatterDiagram():
    x = []
    y = []
    for coord in data:
        x.append(coord[0])
        y.append(coord[1])
    displayCoordinateGraph(x,y)

createScatterDiagram()