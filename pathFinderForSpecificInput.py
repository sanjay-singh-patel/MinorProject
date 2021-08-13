import cv2 as cv
from Search import *
import numpy as np

# Open CV Initialize

img = cv.imread("images/maze-1.jpeg", cv.IMREAD_GRAYSCALE)
_, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)


# Initialize Points

start = (398, 351)
end = (433, 457)

path = astar(img, start, end)

for p in path:
    print(p)
    # img[p.y][p.x] = [100,100,100]



cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()