import cv2
import numpy as np

select_img=input("Enter image path: ")
img=cv2.imread(select_img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,[contour],0,(0,255,0),2)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)#Detect shape by corners
    len_approx=len(approx)

    if len_approx==3:
        shape_name="Triangle"
        
    elif len_approx==4:
        shape_name="Quadrilateral"
        if cv2.isContourConvex(approx):
            shape_name="Square"
        else:
            shape_name="Rectangle"
