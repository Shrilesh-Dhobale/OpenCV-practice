import cv2

image=cv2.imread('../img.jpg')#use to load img

if image is None:
    print("Could not read the image.")

else:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#convert to gray
    if gray is None:
        print("Could not convert to gray.")
    else:
        print("Image converted to gray successfully.")
        print("Press 1 to save the gray image.")
        print("Press 2 to exit without saving.")
        select=int(input("Enter your choice: "))
        if select==1:
            cv2.imwrite('gray_image.jpg',gray)#save the gray image
            print("Gray image saved successfully.")
        elif select==2:
            cv2.imshow("gray_image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("Exiting without saving.")