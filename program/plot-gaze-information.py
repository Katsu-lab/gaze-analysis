import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def createScatterDiagram(x,y):
    figure = plt.figure()
    axes = figure.add_subplot()
    axes.patch.set_facecolor('#00FF00')
    axes.set_title('Gaze of a PC screen(From Bereaved family)')
    line, = plt.plot(x[0], y[0], c='red', marker='.')
    plt.xlim([0,3840])
    plt.ylim([0,2160])

    def update(i):
        line.set_data(x[:i], y[:i])

    ani = animation.FuncAnimation(figure, update)
    plt.show()

def setCsvData():
    data = pd.read_csv('../data/gaze.csv').values.tolist()

    xCoordinateOnScreen = 0
    yCoordinateOnScreen = 1
    milliSecTimeInEyetracker = 2
    milliSecTimeInSystem = 3
    startTimeInConversation = 4

    x = [ column[xCoordinateOnScreen] for column in data ]
    y = [ column[yCoordinateOnScreen] for column in data ]

    return x,y

def displayScatterDiagram():
    gaze = setCsvData()
    xCoordinate = 0
    yCoordinate = 1
    createScatterDiagram(gaze[xCoordinate],gaze[yCoordinate])

displayScatterDiagram()