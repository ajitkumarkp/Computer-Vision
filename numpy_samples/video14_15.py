
## To show the differene between 
## cv2.imshow- BGR format v/s plt.imshow- RGB format

import numpy as np 
import cv2
import matplotlib.pyplot as plt


blank= np.zeros((512,512,3))

print(blank.shape)

cv2.rectangle(blank,(255,255),(400,400),color=(255,255,0),thickness=5)

cv2.circle(blank, (200,400),10,(255,0,0),5)

cv2.line(blank, (0,0), (512,512), (25,0,0),thickness=20)

font= cv2.FONT_HERSHEY_COMPLEX
cv2.putText(blank, "Hello World!", (100,450), font, 1, (255,255,255),4,cv2.LINE_AA)

cv2.imshow("Blank", blank)

plt.imshow(blank)
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()