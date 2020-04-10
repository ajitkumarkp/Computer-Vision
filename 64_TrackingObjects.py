
# ##### From Udemy #####################
# import numpy as np
# import cv2 as cv
# import matplotlib.pyplot as plt

# print("Enter the type of tracing method:")
# print("0- for BOOSTING")
# print("1- for MIL")
# print("2- for KCF")
# print("3- for TLD")
# print("4- for MedianFlow")

# choice = int(input("Enter your choice-- "))

# if choice == 0:
#     tracker = cv.TrackerBoosting_create()
# elif choice == 1:
#     tracker = cv.TrackerMIL_create()
# elif choice == 2:
#     tracker = cv.TrackerKCF_create()
# elif choice == 3:
#     tracker = cv.TrackerBoosting_create()

# cv.namedWindow("tracking")
# cap = cv.VideoCapture(0)
# ret, frame = cap.read()

# roi = cv.selectROI("tracking", frame)

# ret = tracker.init(frame,roi)


# while True:
#     ret, frame = cap.read()
#     success, roi_new = tracker.update(frame)

#     x= int(roi_new[0])
#     y= int(roi_new[1])
#     w= int(roi_new[2])
#     h= int(roi_new[3])

#     if success:
#         cv.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3)
#     else:
#         cv.putText(frame, "Lost Tracking", (100,200), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255),3)

#     cv.imshow("Tracking", frame)

#     if cv.waitKey(0)& 0xFF == 27:
#         break

# cv.destroyAllWindows()
# cap.release()

# ##### opencv github samples #####################

import numpy as np
import cv2 as cv
import sys

cv.namedWindow("tracking")
camera = cv.VideoCapture(0)
ok, image=camera.read()
if not ok:
    print('Failed to read video')
    exit()
bbox = cv.selectROI("tracking", image)
tracker = cv.TrackerMIL_create()
init_once = False

while camera.isOpened():
    ok, image=camera.read()
    if not ok:
        print ('no image to read')
        break

    if not init_once:
        ok = tracker.init(image, bbox)
        init_once = True

    ok, newbox = tracker.update(image)
    print (ok, newbox)

    if ok:
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        cv.rectangle(image, p1, p2, (200,0,0))

    cv.imshow("tracking", image)
    k = cv.waitKey(1) & 0xff
    if k == 27 : break # esc pressed

cv.destroyAllWindows()
camera.release()
