# Object-Detector
# This project recognizes any green object when placed in front of the camera.
# In this project, two libraries are used, first one is opencv and the other one is numpy.
# The desired result is shown with the help of three frames namely, mask, maskOpen and maskClose.
# In mask frame, the green object is detected but the noise in the frame is very high which is reduced
# in maskOpen frame and more reduced in maskClose frame. Moreover, the green section of any object which comes
# in front of the camera is outlined by a blue line whicb makes it more convenient to recognize the green
# section present in the camera frame.

import cv2
import numpy as np

lowerBound = np.array([33,80,40])
upperBound = np.array([102,255,255])

cam = cv2.VideoCapture(0)
kernelOpen = np.ones((5,5))
kernelClose = np.ones((20,20))


while True:
    ret, img = cam.read()
    img = cv2.resize(img,(340,220))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(imgHSV,lowerBound,upperBound)

    maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal = maskClose

    conts,h = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,conts,-1,(255,0,0))

    cv2.imshow("cam",img)
    cv2.imshow("mask",mask)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("maskClose",maskClose)
    cv2.waitKey(10)
