import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def set_data(fileName):
    data = pd.read_csv(config.get('CSV', 'Path') + fileName).values.tolist()

    X_COORDINATE_ON_SCREEN = 0
    Y_COORDINATE_ON_SCREEN = 1
    MILLI_SEC_TIME_IN_EYETRACKER = 2
    MILLI_SEC_TIME_IN_SYSTEM = 3
    ELAPSED_TIME_SINCE_BEGINING_OF_CONVERSATION = 4

    x = [ column[X_COORDINATE_ON_SCREEN] for column in data ]
    y = [ column[Y_COORDINATE_ON_SCREEN] for column in data ]
    t = [ column[ELAPSED_TIME_SINCE_BEGINING_OF_CONVERSATION] for column in data ]

    return x, y, t