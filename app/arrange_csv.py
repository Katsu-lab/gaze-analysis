import configparser
import pandas as pd
import numpy as np

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

def make_elapsed_time_since_last(elapsed_time_list):
    new_elapsed_time_list = [0]
    difference = np.diff(elapsed_time_list)

    new_elapsed_time_list.extend(difference)
    return new_elapsed_time_list

def set_data(fileName):
    data = pd.read_csv(config.get('CSV', 'Path') + fileName).values.tolist()

    x = [ column[config.getint('CSV', 'X_COORDINATE_ON_SCREEN_COLUMN')] for column in data ]
    y = [ column[config.getint('CSV', 'Y_COORDINATE_ON_SCREEN_COLUMN')] for column in data ]
    t = [ column[config.getint('CSV', 'ELAPSED_TIME_SINCE_BEGINING_OF_CONVERSATION_COLUMN')] for column in data ]

    n_t = make_elapsed_time_since_last(t)

    return x, y, t, n_t