import cv2

print("~~~~~~~~~~~~~~Welcome to Shape Drawer~~~~~~~~~~~~~~")

select_img=input("Enter image path: ")
img=cv2.imread(select_img)


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
    print("Rectangle drawn successfully!")
    print("1.To View\n2.To Save")
    view_or_save=input("Enter your choice: ")
    if view_or_save=='1':
        cv2.imshow("Image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif view_or_save=='2':
        save_path=input("Enter path to save image: ")
        cv2.imwrite(save_path,img)
        print("Image saved successfully!")
    else:
        print("Invalid choice!")
elif operation=='2':
    center_x=int(input("Enter x coordinate of center: "))
    center_y=int(input("Enter y coordinate of center: "))
    radius=int(input("Enter radius: "))
    color_b=int(input("Enter blue color value(0-255): "))
    color_g=int(input("Enter green color value(0-255): "))
    color_r=int(input("Enter red color value(0-255): "))
    thickness=int(input("Enter thickness value(positive integer): "))
    img=cv2.circle(img,(center_x,center_y),radius,(color_b,color_g,color_r),thickness)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Circle drawn successfully!")
    print("1.To View\n2.To Save")
    view_or_save=input("Enter your choice: ")
    