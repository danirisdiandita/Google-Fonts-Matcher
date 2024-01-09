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

threshold = 0.9 
chars = [] 

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

        # if the area consists > 90% then its the background then remove it 
    if (x2 - x1)  * (y2 - y1) < threshold * imgray.shape[0] * imgray.shape[1]: 
        chars.append([x1,y1,x2,y2])

    # im = cv.rectangle(im, (x1,y1), (x2, y2), color, thickness)
# remove rectangle that is inside other rectangle 
to_removes = set([])

for i in range(0, len(chars)): 
    for j in range(i+1, len(chars)): 
        # check if i is inside j 
        x1, y1, x2, y2 = chars[i]
        X1, Y1, X2, Y2 = chars[j]
        if x1 >= X1 and x2 <= X2 and y1 >= Y1 and y2 <= Y2:
            to_removes.add(i)
        # check if j is inside i
        if X1 >= x1 and X2 <= x2 and Y1 >= y1 and Y2 <= y2: 
            to_removes.add(j)

chars = [chars[i] for i in range(0, len(chars)) if i not in to_removes] 

# merge the possible of i and j (i and j has that dot over on top)
merger = {}
to_merge = set([])
for i in range(0, len(chars)): 
    for j in range(i+1, len(chars)): 
        x1, y1, x2, y2 = chars[i]
        X1, Y1, X2, Y2 = chars[j]

        # if area is < 1/3 of the later, x axis is in the intersection and the y axis is not too far 
        # intersection = 
        if (x2 - x1) * (y2 - y1) < (X2 - X1) * (Y2 - Y1) / 3 and x1 <= X2 and x2 >= X1  and (y1 - Y2) < Y2 / 3:
            # merge two values 
            merger[i] = j 
            to_merge.add(i)
            to_merge.add(j)
     
            

        if (X2 - X1) * (Y2 - Y1) < (x2 - x1) * (y2 - y1) / 3 and X1 <= x2 and X2 >= x1 and (Y1 - y2) < y2 / 3: # and (y2 - Y1) < y2 / 3: 
            # merge two values
            merger[j] = i 
            to_merge.add(i)
            to_merge.add(j)

newchars = [] 

for i in range(0, len(chars)): 
    if i not in to_merge: 
        newchars.append(chars[i])

for key in merger: 
    x1, y1, x2, y2 = chars[key]
    X1, Y1, X2, Y2 = chars[merger[key]]
    newchars.append([min(X1, x1), min(Y1, y1), max(x2, X2), max(y2, Y2)])

chars = newchars

for i, ( x1, y1, x2, y2 ) in enumerate(chars): 
    cv.rectangle(im, (x1,y1), (x2, y2), color, thickness)
   
    cv.putText(im, f'{i}', (int((x1 + x2)/2), int((y1+y2)/2)), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    

cv.imwrite(f'output_{i:03}.png', im)

