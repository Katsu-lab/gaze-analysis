import cv2
import pandas as pd
import time

import gaze_csv_setting
from orality_calculation import return_gaze_object, return_facial_expression, return_paralanguage

video = cv2.VideoCapture("../data/original/screen_b.mp4")
csv = gaze_csv_setting.CsvSetting()

filePath = "../data/original/gaze_b.csv"
data = pd.read_csv(filePath).values.tolist()
resize = round(3840 / video.get(cv2.CAP_PROP_FRAME_WIDTH))
xList = [ round(column[0] / resize)  for column in data ]
yList = [ round(column[1] / resize) for column in data ]
tList = [ round(column[2]) for column in data ]
tList = csv.make_elapsed_time_since_last(tList)

tList[0] = 1
index = 0
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size=(width, height)
frame_rate = float(video.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
save = cv2.VideoWriter('../data/result/plotted_movie_n.mp4',fourcc,frame_rate,size)

mili_second = frame_rate / 1000

if (video.isOpened()== False):
  print("Error: Can't open this video")

def inputGaze(frame, index):
  coordinate = (xList[index], yList[index])
  cv2.circle(frame, coordinate, 3, (0, 255, 0), -1)
  cv2.putText(frame, "Gaze: " + return_gaze_object.calculate_bereavement_coordinate_information(xList[index], yList[index], resize), (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

def inputFace(frame):
  cv2.putText(frame, "Face: " + return_facial_expression.example(), (10, 60), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

def inputVoice(frame):
  cv2.putText(frame, "Voice: " + return_paralanguage.example(), (10, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

while video.isOpened():
  ret, frame = video.read()

  inputGaze(frame, index)
  inputFace(frame)
  inputVoice(frame)
  time.sleep(mili_second)
  save.write(frame)

  index += 1

save.release()
cv2.destroyAllWindows()