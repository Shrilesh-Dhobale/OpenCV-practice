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

print("Choose operation to perform on image")
print("1. Resize\n2. Rotate\n3. Flip\n4. Convert to Grayscale\n5. Crop\n6. Exit")

operation = input("Enter the number of the operation you want to perform: ")

if operation == '1':
    # Resize the image
    new_width = int(input("Enter new width: "))
    new_height = int(input("Enter new height: "))
    resized_image = cv2.resize(image, (new_width, new_height))
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif operation == '2':
    # Rotate the image
    angle = int(input("Enter rotation angle (in degrees): "))
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif operation == '3':
    # Flip the image
    flip_code = int(input("Enter flip code (0: x-axis, 1: y-axis, -1: both): "))
    flipped_image = cv2.flip(image, flip_code)
    cv2.imshow("Flipped Image", flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif operation == '4':
    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif operation == '5':
    # Crop the image
    x = int(input("Enter x coordinate of top-left corner: "))
    y = int(input("Enter y coordinate of top-left corner: "))
    w = int(input("Enter width of the crop area: "))
    h = int(input("Enter height of the crop area: "))
    cropped_image = image[y:y+h, x:x+w]
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
