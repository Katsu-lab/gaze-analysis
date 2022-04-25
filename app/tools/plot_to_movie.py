import cv2
import gaze_csv_setting

csv = gaze_csv_setting.CsvSetting()
csv.set_data('NURSE')

cap = cv2.VideoCapture(r'../../data/screen_n.avi')

if (cap.isOpened()== False):
  print("Error: Can't open this video")

def setCoordinate():
  coordinate = (300, 300)
  return coordinate

def showFrame(frame):
  coordinate = setCoordinate()
  cv2.circle(frame, coordinate, 3, (0, 0, 255), -1)
  cv2.imshow("Nurse's Gaze on PC screen", frame)

while(cap.isOpened()):
  ret, frame = cap.read()
  # showFrame(frame)

  if ret == True:
      showFrame(frame)

      if cv2.waitKey(25) & 0xFF == ord('q'):
          break

  else:
      break

cv2.destroyAllWindows()