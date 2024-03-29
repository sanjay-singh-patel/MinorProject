# Import packages
import cv2
import tkinter as tk
from tkinter import simpledialog
import json

ROOT = tk.Tk()


# Lists to store the bounding box coordinates
top_left_corner=[]
bottom_right_corner=[]
doors={}

def saveRooms(doors):
  print("saving...")
  with open("Rooms.json", "w") as outfile:
      json.dump(doors, outfile)

# function which will be called on mouse input
def selectDoor(action, x, y, flags, *userdata):
    # Mark the top left corner when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONUP:
        door = (y,x)
        cv2.circle(image, (x,y), 5, (255,0,0))
        ROOT.withdraw()
        # the input dialog
        USER_INP = simpledialog.askstring(title="Test", prompt="What's the Door Name?:")
        doors.update({str(door):USER_INP})
        print(doors)
        cv2.imshow("Window",image)

# Read Images
image = cv2.imread("./images/dept.jpg")
image = cv2.resize(image, (800,400))
# Make a temporary image, will be useful to clear the drawing
temp = image.copy()
# Create a named window
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", selectDoor)

k=0
# Close the window when key q is pressed
while k!=113:
  # Display the image
  cv2.imshow("Window", image)
  k = cv2.waitKey(0)
  # If c is pressed, clear the window, using the dummy image
  if k == 99:
    image= temp.copy()
    cv2.imshow("Window", image)
  if k == 115:
    saveRooms(doors)

cv2.destroyAllWindows()
