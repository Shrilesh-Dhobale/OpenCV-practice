import cv2
import numpy as np

select_img=input("Enter image path: ")
img=cv2.imread(select_img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)