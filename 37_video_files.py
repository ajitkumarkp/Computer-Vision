import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

## Capture object
cap = cv.VideoCapture(0)

fps = cap.get(cv.CAP_PROP_FPS)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print ("FPS, W, H:", fps, width, height)

while True:
    ## Read the frames
    ret, frame = cap.read()

    ## Draw a fixed rectangle on the screen
    cv.rectangle(frame, (width//2, height//2), (width//2+100, height//2+100), color=(255,0,0), thickness=10)

    ## Display frames
    cv.imshow("cam", frame)

    if cv.waitKey(1)&0xFF== ord('q'):
        break


## Destroy/Release objects
cv.destroyAllWindows(0)
cap.release()




