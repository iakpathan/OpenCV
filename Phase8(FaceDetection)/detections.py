import cv2

# Load cascades (make sure paths are correct!)
face_cascade = cv2.CascadeClassifier(r'Phase8(FaceDetection)\haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier(r'Phase8(FaceDetection)\haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(r'Phase8(FaceDetection)\haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # For each face, detect eyes and smiles inside ROI
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)

        # Detect smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.1, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smiling", (x, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Webcam Face Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting")
        break

cap.release()
cv2.destroyAllWindows()