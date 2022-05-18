import configparser
import pandas as pd
import numpy as np

config = configparser.ConfigParser()
config.read('../config.ini', encoding='utf-8')

class CsvSetting():

    def __init__(self):
        self.file_path = config.get('CSV', 'Path')
        self.x_coodinate = config.getint('CSV', 'X_coodinate_on_screen_column')
        self.y_coodinate = config.getint('CSV', 'Y_coodinate_on_screen_column')
        self.time_coodinate = config.getint('CSV', 'Elapsed_time_since_begining_of_conversation_column')

    def make_elapsed_time_since_last(self, elapsed_time_list):
        new_elapsed_time_list = [0]
        difference = np.diff(elapsed_time_list)

        new_elapsed_time_list.extend(difference)
        return new_elapsed_time_list

    def set_data(self, fileName):
        dataSet = pd.read_csv(self.file_path + fileName).values.tolist()

        x = [ data[self.x_coodinate] for data in dataSet ]
        y = [ data[self.y_coodinate] for data in dataSet ]
        t = [ data[self.time_coodinate] for data in dataSet ]

        n_t = self.make_elapsed_time_since_last(t)

        return x, y, t, n_t