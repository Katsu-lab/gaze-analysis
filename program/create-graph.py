import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def createScatterDiagram(x,y):
    figure = plt.figure()
    axes = figure.add_subplot()
    axes.patch.set_facecolor('#00FF00')
    axes.set_title('Gaze of a PC screen(From Bereaved family)')
    scat = axes.scatter(x,y,c='red',marker='.')
    plt.xlim([0,3840])
    plt.ylim([0,2160])
    plt.show()

def setCsvData():
    data = pd.read_csv('../data/gaze.csv').values.tolist()

    xCoordinateOnScreen = 0
    yCoordinateOnScreen = 1
    milliSecTimeInSystem = 2
    startTimeInConversation = 3

    x = [ coord[xCoordinateOnScreen] for coord in data ]
    y = [ coord[yCoordinateOnScreen] for coord in data ]

    return x,y

def displayScatterDiagram():
    gaze = setCsvData()
    xCoordinate = 0
    yCoordinate = 1
    createScatterDiagram(gaze[xCoordinate],gaze[yCoordinate])

displayScatterDiagram()