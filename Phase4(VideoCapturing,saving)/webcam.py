import cv2
cap= cv2.VideoCapture(0)
while True:
    fine,frame=cap.read()
    if not fine:
        print(" Couldnt read frame")
        break
    cv2.imshow("Webcam Feed",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Quitting")
        break
cap.release()
cv2.destroyAllWindows()


    