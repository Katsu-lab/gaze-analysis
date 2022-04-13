import csv

def output_data(time, gaze, face, voice):
    f = open('../data/result.csv', 'a')
    data = [time, gaze, face, voice]
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()