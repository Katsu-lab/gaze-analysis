import cv2

care_movie = cv2.VideoCapture('../../data/screen_n.mp4')
print(type(care_movie))
print(care_movie.isOpened())

print(care_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
print(care_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(care_movie.get(cv2.CAP_PROP_FPS))
print(care_movie.get(cv2.CAP_PROP_FRAME_COUNT))