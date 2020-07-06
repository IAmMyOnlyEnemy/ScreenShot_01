from PIL import ImageGrab

#Pillow.ImageGrab.grab(bbox=None)


frame = (0, 0, 1900, 1080)
img = ImageGrab.grab(bbox=frame)
print(type(img))
img.save("BBBBBB.jpg", "jpeg")

'''
from PIL import ImageGrab
import time

time.sleep(5)
ImageGrab.grab().save("screen_capture.jpg", "JPEG")
'''
