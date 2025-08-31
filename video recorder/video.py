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
    print("Recording... Press 'v' to view.")
    print("Press 's' to save without viewing.")

    if cv2.waitKey(1) & 0xFF == ord('v'):
        cv2.imshow("Video", frame)
        print("Press 'q' to stop recording.")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            print("Recording stopped.")
            print("Would you like to save the recording? (y/n)")
            if cv2.waitKey(1) & 0xFF == ord('y'):
                out.write(frame)
                print("Recording saved.")
            else:
                cv2.destroyAllWindows()
                print("Recording discarded.")
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        out.write(frame)
        print("Frame saved.")
