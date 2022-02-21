import configparser

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def createScatterDiagram(x, y, t, user):
    figure = plt.figure()
    axes = figure.add_subplot(config.getint(user, 'PlotNumber'))
    axes.patch.set_facecolor('#00FF00')
    plt.xlim([0, config.getint('PC', 'Width')])
    plt.ylim([0, config.getint('PC', 'Height')])

    def update(i):
        if i != 0:
            plt.plot(linewidth=None)

        line, = plt.plot(x[0], y[0], c='red', marker='.')
        line.set_data(x[:i], y[:i])
        time = str(t[:i])
        axes.set_title('Gaze on PC screen(From ' + config.get(user, 'Username') + ')')

    ani = animation.FuncAnimation(figure, update, interval = 30)
    # ani.save('../../plot.gif', writer='ffmpeg', dpi=300)
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
    t = [ column[elapsedTimeSinceBeginingOfConversation] for column in data ]

    return x, y, t

def displayScatterDiagram(user):
    if user == 'b':
        user = 'BEREAVED FAMILY'
    elif user == 'n':
        user = 'NURSE'
    elif user == 'a':
        user = 'ALL'

    gaze = setCsvData(config.get(user, 'Gaze'))
    xCoordinate = 0
    yCoordinate = 1
    elapsedTime = 2
    createScatterDiagram(gaze[xCoordinate], gaze[yCoordinate], gaze[elapsedTime], user)

def displayScatterDiagrams(user1,user2):
    displayScatterDiagram(user1)
    displayScatterDiagram(user2)

print("Whose gaze information do you want 'BEREAVED FAMILY' or 'NURSE' or ALL ?")
user = input("Please enter b/n/a : ")
print("Which gaze plot mode do you want 'SINGLE' or 'MULTIPLE' ?")
mode = input("Please enter s/m : ")
displayScatterDiagram('BEREAVED FAMILY')