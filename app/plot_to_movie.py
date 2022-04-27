import cv2
from matplotlib.pyplot import xlabel
import pandas as pd
import gaze_csv_setting

video = cv2.VideoCapture("../data/screen_n.mp4")
csv = gaze_csv_setting.CsvSetting()

size=(640,480)
frame_rate = int(video.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
save = cv2.VideoWriter('../data/plotted_movie.mp4',fourcc,frame_rate,size)

filePath = "../data/gaze_n.csv"
data = pd.read_csv(filePath).values.tolist()
resize = 4.5
xList = [ round(column[0] / resize)  for column in data ]
yList = [ round(column[1] / resize) for column in data ]
tList = [ round(column[2]) for column in data ]
tList = csv.make_elapsed_time_since_last(tList)

tList[0] = 1
index = 0

if (video.isOpened()== False):
  print("Error: Can't open this video")

def showFrame(frame, index):
  coordinate = (xList[index], yList[index])
  cv2.circle(frame, coordinate, 3, (0, 0, 255), -1)
  save.write(frame)
  cv2.imshow("Nurse's Gaze on PC screen", frame)

while video.isOpened():
  ret, frame = video.read()

  if ret == True:
      showFrame(frame, index)

      if cv2.waitKey(tList[index]) & 0xFF == ord('q'):
          break

  else:
      break

  index += 1

save.release()
cv2.destroyAllWindows()