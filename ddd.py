import cv2
import numpy as np
import time


cap = cv2.VideoCapture('6.mp4')

while True:

    raw_image, frame = cap.read()
    #raw_image = cv2.imread('rawImage.jpg')
    #cv2.imshow('Original Image', raw_image)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([48, 0, 0])
    upper_blue = np.array([179, 117, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    bilateral_filtered_image = cv2.bilateralFilter(mask, 5, 175, 175)

    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    edge_detected_image1 = cv2.Canny(edge_detected_image, 75, 200)
    _, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
            contour_list.append(contour)

    cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
    cv2.imshow('Bilateral', bilateral_filtered_image)
    cv2.imshow('Edge', edge_detected_image)
    cv2.imshow("edge1", edge_detected_image1)
    cv2.imshow('Objects Detected',raw_image)
    time.sleep(0.25)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
