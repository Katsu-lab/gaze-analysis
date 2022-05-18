import csv
import pandas as pd

facial_types = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sadness', 'Surprise', 'Contempt','Neutral']
au_rules = [[4,5,15,17], [1,4,15,17], [1,4,7,20], [6,12,25], [1,2,4,15,17], [1,2,5,25,27], [14]]

file_name = 'face_n.csv'
file_path = '../../data/original/' + file_name
edited_file_name = 'simple_action_unit_n.csv'
edited_file_path = '../data/result/' + edited_file_name

def organize_facial_data():
    f = open('../../data/result/organized_au_' + file_name, 'a')
    dataSet = pd.read_csv(file_path).values.tolist()
    writer = csv.writer(f)
    for data in dataSet:
        writer.writerow(data[0:4] + data[679:])
    f.close()

def check_header_names():
    df=pd.read_csv(file_path, header=0)
    header=df.columns
    print(header[0:4] + header[679:]) #This is begining of AU column

def create_simple_au_data_set():
    f = open('../../data/result/organized_simple_au_' + file_name, 'a')
    dataSet = pd.read_csv(file_path).values.tolist()
    writer = csv.writer(f)
    for data in dataSet:
        writer.writerow(data[2:3] + data[696:])
    f.close()

def create_complex_au_data_set():
    f = open('../../data/result/organized_complex_au_' + file_name, 'a')
    dataSet = pd.read_csv(file_path).values.tolist()
    writer = csv.writer(f)
    for data in dataSet:
        writer.writerow(data[2:3] + data[679:696])
    f.close()

def change_index_to_au_number(au_list):
    au_numbers = [0,1,2,4,5,6,7,9,10,12,14,15,17,20,23,25,26,28,45]
    true_au_list = []
    for au_index in au_list:
        true_au_list.append(au_numbers[au_index])
    return true_au_list


def get_active_au():
    f = open('../data/result/analyzed_' + edited_file_name, 'a')
    data_set = pd.read_csv(edited_file_path).values.tolist()
    writer = csv.writer(f)
    for data in data_set:
        facial_expression = facial_types[7] # If there is nothing special, return neutral as facial expression
        active_au_list = [i for i, n in enumerate(data) if n == 1.0]
        active_au_list = change_index_to_au_number(active_au_list)
        for i, rule in enumerate(au_rules):
            if set(rule) == (set(rule) & set(active_au_list)):
                facial_expression = facial_types[i]
                break

        writer.writerow([data[0], active_au_list, facial_expression])
    f.close()