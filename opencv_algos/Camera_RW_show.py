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

## Writer object
writer = cv.VideoWriter("myvideo.mp4", cv.VideoWriter_fourcc(*'DIVX'),fps, (width,height))

while True:
    ## Read the frames
    ret, frame = cap.read()
    ## Display frames
    cv.imshow("cam", frame)
    ## Write to file
    writer.write(frame)

    if cv.waitKey(1)&0xFF== ord('q'):
        break

## Destroy/Release objects
cv.destroyAllWindows(0)
cap.release()
writer.release()
