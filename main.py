import cvzone
import numpy as np
import pickle
import cv2

img = cv2.imread('parking_image.png')
width, height = 24, 50

with open('CarParkPosition', 'rb') as f:
    posList = pickle.load(f)


def checkParkingSpace(imgPro):
    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=1, offset=0)

        if count < 275:
            color = (0, 255, 0)
            thickness = 2
        else:
            color = (0, 0, 255)
            thickness = 2
        radius = 2
        cv2.circle(img, (x + width // 2, y + height // 2), radius, color, thickness)


        # Draw dots instead of rectangles

while True:
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThreshold",imgThreshold)
    cv2.imshow("ImageMed",imgMedian)
    cv2.waitKey(1)

  # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThreshold",imgThreshold)
    # cv2.imshow("ImageMed",imgMedian)