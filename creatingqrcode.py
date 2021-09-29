#This creates a unique QR Code for each co-ordinate

import pyqrcode
import png
from pyqrcode import QRCode
import json
f = open("Rooms.json")
Rooms = json.load(f)
for i in Rooms:
    url = pyqrcode.create(i)
    url.svg("myqr"+i+".svg",scale = 8)
    url.png("myqr"+i+".png",scale = 6)
