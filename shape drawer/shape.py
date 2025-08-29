import cv2

print("~~~~~~~~~~~~~~Welcome to Shape Drawer~~~~~~~~~~~~~~")

img=input("Enter image path: ")

print("Press 1 to draw a rectangle")
print("Press 2 to draw a circle")
print("Press 3 to draw a line")
print("Press 4 to add text")
print("Press 5 to exit")

operation=input("Enter your choice: ")

if operation=='1':
    pt1_x=int(input("Enter x coordinate of point 1: "))
    pt1_y=int(input("Enter y coordinate of point 1: "))
    pt2_x=int(input("Enter x coordinate of point 2: "))
    pt2_y=int(input("Enter y coordinate of point 2: "))
    color_b=int(input("Enter blue color value(0-255): "))
    color_g=int(input("Enter green color value(0-255): "))
    color_r=int(input("Enter red color value(0-255): "))
    thickness=int(input("Enter thickness value(positive integer): "))
    img=cv2.rectangle(img,(pt1_x,pt1_y),(pt2_x,pt2_y),(color_b,color_g,color_r),thickness)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
