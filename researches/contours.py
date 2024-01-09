import numpy as np
import cv2 as cv
im = cv.imread('test.png')
assert im is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours[0])

color = (0, 0, 255)
thickness = 5


for k in range(0, len(contours)):
    x1 = np.inf 
    x2 = 0 
    y1 = np.inf 
    y2 = 0 
    
    for i in range(0, contours[k].shape[0]): 
        x,y = contours[k][i][0]
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)

    im = cv.rectangle(im, (x1,y1), (x2, y2), color, thickness)
cv.imwrite('output.png', im)

