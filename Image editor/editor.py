import cv2
print("Welcome to Image Editor!!")
select_image = input("Please select an image file: ")
image = cv2.imread(select_image)  # use to load image
