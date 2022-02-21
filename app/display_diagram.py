import configparser
import matplotlib.pyplot as plt
import arrange_csv as csv
import create_diagram as create

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def scatter_diagram(user):
    if user == 'b':
        user = 'BEREAVED FAMILY'
    elif user == 'n':
        user = 'NURSE'
    elif user == 'a':
        user = 'ALL'

    gaze = csv.set_data(config.get(user, 'Gaze'))
    xCoordinate = 0
    yCoordinate = 1
    elapsedTime = 2
    create.scatter_diagram(gaze[xCoordinate], gaze[yCoordinate], gaze[elapsedTime], user)
    # plt.show()

def scatter_diagrams():
    gaze1 = csv.set_data(config.get('BEREAVED FAMILY', 'Gaze'))
    gaze2 = csv.set_data(config.get('NURSE', 'Gaze'))
    xCoordinate = 0
    yCoordinate = 1
    create.scatter_diagrams(gaze1[xCoordinate], gaze1[yCoordinate], gaze2[xCoordinate], gaze2[yCoordinate])