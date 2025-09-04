import cv2

face_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("c:\\Users\\Shrilesh\\Desktop\\OpenCV practice\\object & face detection\\haarcascade_smile.xml")

cap=cv2.VideoCapture(0)

while True:
    rel, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Detect fast and accurate

    faces=face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
        # The condition should be > 0 to confirm detection.
        if len(eyes) > 0:
            cv2.putText(frame,"Eyes Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        smiles=smile_cascade.detectMultiScale(roi_gray,1.7,12)
        if len(smiles) > 0:
            cv2.putText(frame,"Smiling",(x,y-8),cv2.FONT_HERSHEY_SIMPLEX,1,(120,120,120),2)
        if len(smiles) == 0:
            cv2.putText(frame,"Not Smiling",(x,y-8),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    