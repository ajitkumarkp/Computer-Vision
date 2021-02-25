import numpy as np
import cv2

white= (255,255,255)
blue=  (255,0,0)
green= (0,255,0)
red=   (0,0,255)

# Global variables

color= blue
radius= 3

canvas = np.ones((1000,1000,3),'uint8')*255
pressed = False	

# click callback
def click(event, x, y, flags, param):
    global canvas, pressed, color, radius
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas,(x,y),radius=radius,color=color,thickness=-1)
        pressed=True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if pressed:
            cv2.circle(canvas,(x,y),radius,color,-1)
			# cv2.circle(canvas, (x,y),radius,color,width)

    elif event == cv2.EVENT_LBUTTONUP:
        pressed=False

    elif event == cv2.EVENT_RBUTTONDOWN:
        if color==blue: color=green
        elif color==green: color=red
        elif color==red: color=blue
        elif color==white: color, radius= blue, 3


# window initialization and callback assignment
cv2.namedWindow("canvas- press q to quit, n for new canvas, e to erase")
cv2.setMouseCallback("canvas- press q to quit, n for new canvas, e to erase", click)

# Forever draw loop
while True:
    cv2.imshow("canvas- press q to quit, n for new canvas, e to erase",canvas)
	# key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    if ch & 0xFF == ord('n'):
        canvas = np.ones([1000,1000,3],'uint8')*255
    if ch & 0xFF == ord('e'):
        color, radius = white, 6

cv2.destroyAllWindows()
