import cv2
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0,6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

img = cv2.imread("musk.jpg")
sunglass = cv2.imread("sunglass.png", -1)

DNN = "CAFFE"
if DNN == "CAFFE":
    modelFile = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = "deploy.prototxt"
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
else:
    modelFile = "opencv_face_detector_uint8.pb"
    configFile = "opencv_face_detector.pbtxt"
    net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)
    
def detectFaceOpenCVDnn(net, frame):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()

    # print(detections.shape)
    bboxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            # print(confidence)
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            # cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes

conf_threshold = 0.995
output,bboxes = detectFaceOpenCVDnn(net, img)
# print(bboxes)

x1 = bboxes[0][0]
y1 = bboxes[0][1]
x2 = bboxes[0][2]
y2 = bboxes[0][3]

ix1 = 5
ix2 = 280
iy1 = 100
iy2 = 220

# extract the face region
face = output[y1:y2, x1:x2]
face_copy = face.copy()

# extract the eye region
eye_roi = face[iy1:iy2, ix1:ix2]

# Resize the sunglass image to the eye region
sunglass =  cv2.resize(sunglass, (tuple(np.flip(eye_roi.shape[0:2]))))

# Seperate the RGB and Alpha components from the sunglass image
sunglass_rgb = sunglass[...,0:3]
alpha_mask = sunglass[...,3]

# convert to 3 channels for the rest of processing with rgb images
alpha_mask = cv2.merge((alpha_mask, alpha_mask, alpha_mask))

# Create Masks for the eyes and sunglass 
eye_mask = cv2.bitwise_and(eye_roi, cv2.bitwise_not(alpha_mask))
sunglass_mask = cv2.bitwise_and(sunglass_rgb, alpha_mask)

# Read the scenary in GS and create 3 GS channels
scenary = cv2.imread("scenary.png",0)
# scenary = cv2.imread("droplets.png",0)
scenary = cv2.merge((scenary, scenary, scenary))

# Resize scenary
scenary =  cv2.resize(scenary, (tuple(np.flip(eye_roi.shape[0:2]))))

# This is the Scenary mask
scenary = cv2.bitwise_and(scenary, alpha_mask)

# Blending the scenary with the sunglass mask and adding transparency 
alpha = 0.9
sunglass_mask = cv2.addWeighted(sunglass_mask, alpha, scenary, 1-alpha, 0)

# Merging the forground and background masks
final_output = cv2.bitwise_or(eye_mask,sunglass_mask)

# Stitch this into the face image and extract the new eye+sunglass region 
face[iy1: iy2, ix1:ix2] = final_output
new_roi = face[iy1: iy2, ix1:ix2]

# Bleding the new eye+sunglass region with original face and add transparency
alpha = 0.2
final_output = cv2.addWeighted(face_copy[iy1:iy2, 5:ix2], alpha, new_roi, 1-alpha, 0)

# Merge the final image to the orginal image
face[iy1: iy2, ix1:ix2] = final_output
img[y1:y2, x1:x2] = face

# plt.figure(figsize=[5,5])
#plt.subplot(131); 
plt.imshow(img[...,::-1]); plt.title("face")
# plt.subplot(132); plt.imshow(sunglass_mask[...,::-1]); plt.title("sunglass_mask")
# plt.subplot(133); plt.imshow(final_output[...,::-1]); plt.title("final_output")
plt.show()
