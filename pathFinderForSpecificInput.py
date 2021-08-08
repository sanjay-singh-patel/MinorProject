import cv2 as cv
from Search import *

# Open CV Initialize

img = cv.imread("images/maze-1.jpeg", cv.IMREAD_GRAYSCALE)
_, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)


# Initialize Points

start = Point(398, 351)
end = Point(433, 457)

path = BFS(img, start, end)

for p in path:
    print("(", p.x, p.y, end=" ), ")
    # img[p.y][p.x] = [100,100,100]



""" 
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
"""