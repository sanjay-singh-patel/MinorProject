import cv2
import numpy as np
image = cv2.imread("./images/dept.jpg")
image = cv2.resize(image, (800,400))

k=0
# Close the window when key q is pressed
while k!=113:
  # Display the image
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)