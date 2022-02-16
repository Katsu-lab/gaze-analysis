import configparser

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def createScatterDiagram(x, y, t):
    figure = plt.figure()
    axes = figure.add_subplot()
    axes.patch.set_facecolor('#00FF00')
    axes.set_title('Gaze of a PC screen(From Bereaved family)')
    line, = plt.plot(x[0], y[0], c='red', marker='.')
    plt.xlim([0, config.getint('PC', 'WidthDpi')])
    plt.ylim([0, config.getint('PC', 'HeightDpi')])

    def update(i):
        # if i != 0:
        #     plt.cla()

        line.set_data(x[:i], y[:i])

    ani = animation.FuncAnimation(figure, update, interval = 30)
    plt.show()

def setCsvData(fileName):
    data = pd.read_csv('../data/' + fileName).values.tolist()

    xCoordinateOnScreen = 0
    yCoordinateOnScreen = 1
    milliSecTimeInEyetracker = 2
    milliSecTimeInSystem = 3
    elapsedTimeSinceBeginingOfConversation = 4

    x = [ column[xCoordinateOnScreen] for column in data ]
    y = [ column[yCoordinateOnScreen] for column in data ]
    t = [ column[yCoordinateOnScreen] for column in data ]

    return x, y, t

def displayScatterDiagram():
    gaze = setCsvData(config.get('GAZE CSV', 'Name'))
    xCoordinate = 0
    yCoordinate = 1
    elapsedTime = 2
    createScatterDiagram(gaze[xCoordinate], gaze[yCoordinate], gaze[elapsedTime])

displayScatterDiagram()