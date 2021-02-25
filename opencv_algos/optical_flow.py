##### From openCV.org #####################
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))
# print(len(color)) # 100 colors

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
print("p0 is:",p0)

# print(p0)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow using Lucas-Kanade method
    # Given a point on a frame, the algo will estimate where that point is on a new frame.
    # Basically it tracks/follows the orginal point across diff frames. 
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    
    print("New p0 is:",p0)
    
    print("p1 is:",p1)

    # Select good points
    good_new = p1[st==1]
    good_old = p0[st==1]

    # print(good_new)
    # print(good_old)

    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv2.add(frame,mask)

    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv2.destroyAllWindows()
cap.release()

##### From Udemy #####################
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt
# from PIL import Image

# corner_track_parm =  dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)

# lk_params = dict(winSize=(200,200), maxLevel=2, criteria= (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# cap = cv.VideoCapture(0)

# ret, prev_frame = cap.read()

# prev_gray = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)

# # Pts to track
# prev_points = cv.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_parm)
# mask = np.zeros_like(prev_frame)

# while True:
#     ret, frame = cap.read()

#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
#     # calculate optical flow
#     next_pts, status, err = cv.calcOpticalFlowPyrLK(prev_gray, frame_gray, prev_points, None, **lk_params)

#     # select good points
#     good_new = next_pts[status==1]
#     good_prev = prev_points[status==1]

#     # draw the tracks
#     for i, (new, prev) in enumerate(zip(good_new, good_prev)):
#         x_new, y_new = new.ravel()
#         x_prev, y_prev = prev.ravel()

#         mask = cv.line(mask, (x_new, y_new), (x_prev,y_prev), (0,255,0), 3)
#         frame = cv.circle(frame, (x_new,y_new), 8, (0,0,255), -1)

#     img = cv.add(mask, frame)
#     cv.imshow("img", img)

#     if cv.waitKey(30) & 0xFF == 27:
#         break
    
#     prev_gray = frame_gray.copy()
#     prev_points = good_new.reshape(-1,1,2)


# cv.destroyAllWindows()
# cap.release()





