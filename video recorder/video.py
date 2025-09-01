import cv2

print("-----------------Welcome tO Video Recorder------------------")

camera=cv2.VideoCapture(0)

frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec=cv2.VideoWriter_fourcc(*"XVID")
output_file=input("Enter output file name(with extension): ")
fps=int(input("Enter frames per second: "))

out=cv2.VideoWriter(output_file,codec,fps,(frame_width,frame_height))

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to grab frame")
        break
    out.write(frame)
    cv2.imshow("Video Recorder", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()