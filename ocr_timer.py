from PIL import Image
import pytesseract
import argparse
import cv2
import os

import config as cfg

image = cv2.imread('frame_crop.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#gray = cv2.medianBlur(gray, 3)

gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
#os.remove(filename)
print(text)