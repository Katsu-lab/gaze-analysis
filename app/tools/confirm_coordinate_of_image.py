import cv2
import numpy as np
file_name='../assets/img/NURSE.png'
img=cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)

def mouse_move(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        img2 = np.copy(img)
        cv2.circle(img2,center=(x,y),radius=5,color=255,thickness=-1)
        pos_str='(x,y)=('+str(x)+','+str(y)+')'
        cv2.putText(img2,pos_str,(30, 30),cv2.FONT_HERSHEY_PLAIN,2,255,2,cv2.LINE_AA)
        cv2.imshow('window', img2)

cv2.imshow('window', img)
cv2.setMouseCallback('window', mouse_move)
cv2.waitKey(0)
cv2.destroyAllWindows()