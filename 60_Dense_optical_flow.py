# ##### From Opencv.org #####################
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)

# For Coloring based on direction set to max saturation
hsv[...,1] = 255

while(1):

    ret, frame2 = cap.read()
    cv2.imshow('Cam',frame2)
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    # Vector representing the flow of the pixels 
    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Convert from cartesian to Polar coordinates i.e from x,y vetor flow to magnitude and radians
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1], angleInDegrees=True)
    
    # Angle is represented in terms of Hue, from 0 to 180 degrees   
    hsv[...,0] = ang/2

    # Magnitude is represented in terms of Value
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)

    # Blue and Red for Horizontal, Green and Purple for Vertical

    # Convert to BGR for CV imshow
    bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    cv2.imshow('Optical Flow',bgr)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)

    prvs = next

cap.release()
cv2.destroyAllWindows()

# ##### From Udemy #####################
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt

# cap = cv.VideoCapture(0)

# ret, frame1 = cap.read()
# prvsImg = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

# hsv_mask = np.zeros_like(frame1)

# # plt.imshow(hsv_mask), plt.show()

# hsv_mask[:,:,1] = 255

# # print (prvsImg[0,0,1])
# # print (prvsImg[0,0]) 


# while True:

#     ret, frame2 = cap.read()
#     nextImg= cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)

#     flow = cv.calcOpticalFlowFarneback(prvsImg,nextImg,None,0.5,3,15,3,5,1.2,0)

#     mag,ang = cv.cartToPolar(flow[:,:,0], flow[:,:,1], angleInDegrees=True)

#     hsv_mask[:,:,0] = ang/2
#     hsv_mask[:,:,2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)

#     bgr = cv.cvtColor(hsv_mask, cv.COLOR_HSV2BGR)

#     cv.imshow("BGR", bgr)

#     if cv.waitKey(0) & 0xFF == 27:
#         break

#     prvsImg = nextImg

# cv.destroyAllWindows()
# cap.release()



