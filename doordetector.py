import cv2 as cv

img = cv.imread("images/image.png")
bw = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
resized = cv.resize(img,(700,500))
canny = cv.Canny(resized,50,300)
cv.imshow("image",img)
cv.imshow("bw",bw)
cv.imshow("canny",canny)
cv.waitKey(0)