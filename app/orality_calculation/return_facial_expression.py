import csv
import pandas as pd


def calculate_bereavement_facial_expression_information(time):
    data_set = pd.read_csv('../data/result/analyzed_simple_action_unit_b').values.tolist()
    return time

def calculate_nurse_facial_expression_information(time):
    data_set = pd.read_csv('../data/result/analyzed_simple_action_unit_n').values.tolist()
    return time