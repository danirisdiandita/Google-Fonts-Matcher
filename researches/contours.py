import numpy as np
import cv2 as cv
import os 
import argparse 

parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
parser.add_argument(
    '--file', type=str,
    help='file')

args = parser.parse_args()
file = args.file 
im = cv.imread(file)

if os.path.isdir('tmp') == False: 
    os.makedirs('tmp')

outdir, _ = os.path.splitext(os.path.basename(file))
os.popen(f'rm -rf tmp/{outdir}').read()
if os.path.isdir(f'tmp/{outdir}') == False: 
    os.makedirs(f'tmp/{outdir}')

assert im is not None, "file could not be read, check with os.path.exists()"

# blank = np.ones(im.shape) * 255 
blank = np.zeros(im.shape) 
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours[0])

threshold = 0.95 
contours_boolean = [0] * len(contours)
contours_boundaries = [None] * len(contours)
for i in range(0, len(contours)): 
    x1 = np.inf 
    x2 = 0 
    y1 = np.inf 
    y2 = 0 
    for k in range(0, contours[i].shape[0]): 
        x, y = contours[i][k][0]
        x1 = min(x1, x)
        y1 = min(y1, y)
        x2 = max(x2, x)
        y2 = max(y2, y)
    if (x2 - x1)  * (y2 - y1) < threshold * imgray.shape[0] * imgray.shape[1]: 
        cv.drawContours(blank, contours, i, (255, 255, 255), thickness=cv.FILLED)
        contours_boolean[i] = 1 


# cv.imwrite(f'tmp/{outdir}/contours.png', blank)

color = (0, 0, 255)
thickness = 5

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
        # cv.drawContours(blank, contours, k, (255, 255, 255), thickness=cv.FILLED)
        # chars.append([x1,y1,x2,y2])
        contours_boundaries[k] = [x1, y1, x2, y2]


    # im = cv.rectangle(blank, (x1,y1), (x2, y2), color, thickness)

# remove rectangle that is inside other rectangle 
to_removes = set([])

for i in range(0, len(contours_boundaries)): 
    for j in range(i+1, len(contours_boundaries)):
        if contours_boundaries[i] == None or contours_boundaries == None: 
            continue  
        # check if i is inside j 
        x1, y1, x2, y2 = contours_boundaries[i]
        X1, Y1, X2, Y2 = contours_boundaries[j]
        if x1 >= X1 and x2 <= X2 and y1 >= Y1 and y2 <= Y2:
            to_removes.add(i)
        # check if j is inside i
        if X1 >= x1 and X2 <= x2 and Y1 >= y1 and Y2 <= y2: 
            to_removes.add(j)


for i in to_removes: 
    # paint black 
    cv.drawContours(blank, contours, i, (0, 0, 0), thickness=cv.FILLED)

cv.imwrite(f'tmp/{outdir}/contours.png', blank)

# chars = [chars[i] for i in range(0, len(chars)) if i not in to_removes] 

# merge the possible of i and j (i and j has that dot over on top)
merger = {}
to_merge = set([])
for i in range(0, len(contours_boundaries)): 
    for j in range(i+1, len(contours_boundaries)):
        if contours_boundaries[i] == None or contours_boundaries == None: 
            continue  
        if i in to_removes or j in to_removes: 
            continue
        x1, y1, x2, y2 = contours_boundaries[i]
        X1, Y1, X2, Y2 = contours_boundaries[j]

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

for i in range(0, len(contours_boundaries)): 
    if i not in to_merge and i not in to_removes and contours_boundaries[i] != None: 
        newchars.append(contours_boundaries[i])
# print('merger', merger)
for key in merger: 
    x1, y1, x2, y2 = contours_boundaries[key]
    X1, Y1, X2, Y2 = contours_boundaries[merger[key]]
    newchars.append([min(X1, x1), min(Y1, y1), max(x2, X2), max(y2, Y2)])
    print('len(newchars)', len(newchars))

chars = newchars
# print(chars)


for i, ( x1, y1, x2, y2 ) in enumerate(chars): 
    # cv.rectangle(im, (x1,y1), (x2, y2), color, thickness)
    # cv.putText(im, f'{i}', (int((x1 + x2)/2), int((y1+y2)/2)), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    # print(im.shape, x1,y1,x2,y2)

    # im shape shows height, width, dimension 
    # cv.imwrite(f'tmp/output_{i:03}.png', blank[y1:y2,x1:x2,:])

    fontvector = blank[y1:y2,x1:x2,:]
    font_width = fontvector.shape[0]
    font_height = fontvector.shape[1]

    # create a square shape maxwidth or maxheight 
    sidelength = max(font_height, font_width)
    square = np.zeros((sidelength, sidelength, 3))
    # print(square.shape, end=', ')
    square[(sidelength-font_width)//2: (sidelength+font_width)//2,(sidelength-font_height)//2: (sidelength+font_height)//2,:] = fontvector

    # print(blank[y1:y2,x1:x2,:].shape)
    square = cv.resize(square, (250, 250))
    # print(np.max(square, axis=-1).shape)
    
    
    
    cv.imwrite(f'tmp/{outdir}/output_{i:03}.png', square)


# cv.imwrite('blank.png', blank)

# cv.imwrite(f'output_{i:03}.png', im)

