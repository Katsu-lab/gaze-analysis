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

    gaze = csv.set_data(config.get(user, 'Gaze'))
    X_COORDINATE_COLUMN = 0
    Y_COORDINATE_COLUMN = 1
    ELAPSED_TIME_COLUMN = 2
    create.scatter_diagram(gaze[X_COORDINATE_COLUMN], gaze[Y_COORDINATE_COLUMN], gaze[ELAPSED_TIME_COLUMN], user)
    # plt.show()

def scatter_diagrams():
    gaze1 = csv.set_data(config.get('BEREAVED FAMILY', 'Gaze'))
    gaze2 = csv.set_data(config.get('NURSE', 'Gaze'))
    X_COORDINATE_COLUMN = 0
    Y_COORDINATE_COLUMN = 1
    ELAPSED_TIME_COLUMN = 2
    create.scatter_diagrams(gaze1[X_COORDINATE_COLUMN], gaze1[Y_COORDINATE_COLUMN], gaze2[X_COORDINATE_COLUMN], gaze2[Y_COORDINATE_COLUMN])