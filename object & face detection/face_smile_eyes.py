import cv2

face_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_smile.xml")

cap=cv2.VideoCapture(0)

while True:
    rel, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Detect fast and accurate