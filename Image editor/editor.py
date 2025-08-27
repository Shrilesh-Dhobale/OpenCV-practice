import cv2
print("Welcome to Image Editor!!")
select_image = input("Please select an image file: ")
image = cv2.imread(select_image)  # use to load image
if image is None:
    print("Could not read the image.")
else:
    print("Image loaded successfully.")
    # Display the image
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
