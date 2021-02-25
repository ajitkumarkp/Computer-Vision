
## Mouse callback

import numpy as np 
import cv2

canvas= np.zeros((512,512,3))
ox,oy= -1,-1
ldown=False

##callback func
def draw_rect (event, x,y, flags, param):
    global ox,oy,ldown

    cv2.EVENT_FLAG_CTRLKEY

    if event==cv2.EVENT_LBUTTONDOWN:
        ox,oy=x,y
        ldown=True
    
    elif event==cv2.EVENT_LBUTTONUP:
        ldown=False

    elif event==cv2.EVENT_MOUSEMOVE:
        if ldown:
            cv2.rectangle(canvas,(ox,oy),(x,y),color=(255,0,0),thickness=-1)
        
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", draw_rect)

while True:
    cv2.imshow("Canvas", canvas)
    if cv2.waitKey(1) & 0xFF==27:
        break

cv2.destroyAllWindows()
