import cv2
import pickle

img = cv2.imread('parking_image.png')
try:
    with open('CarParkPosition', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

width, height = 24, 50


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open('CarParkPosition', 'wb') as f:
        pickle.dump(posList, f)


while True:
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    # cv2.rectangle(img,(125,100),(155,150),(255,0,255),2)
    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouseClick)
    cv2.waitKey(1)
