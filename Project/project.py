import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

mode = "edges"
prev_frame = None

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml')

def reorder_points(pts):
    pts = pts.reshape((4, 2))
    new_pts = np.zeros((4, 1, 2), dtype=np.int32)

    s = pts.sum(1)
    new_pts[0] = pts[np.argmin(s)]
    new_pts[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    new_pts[1] = pts[np.argmin(diff)]
    new_pts[3] = pts[np.argmax(diff)]

    return new_pts

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    output = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    start_time = time.time()

    # ================= EDGE MODE =================
    if mode == "edges":
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 50, 150)
        output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # ================= COLOR MODE (FIXED) =================
    elif mode == "color":
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Wide blue range (more stable)
        lower = np.array([90, 50, 50])
        upper = np.array([140, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.GaussianBlur(mask, (5,5), 0)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 800:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(output, (x,y), (x+w,y+h), (255,0,0), 2)
                cv2.putText(output, "Blue Object", (x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (255,0,0), 2)

        mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        output = cv2.hconcat([output, mask_color])

    # ================= MOTION =================
    elif mode == "motion":
        blur = cv2.GaussianBlur(gray, (5,5), 0)

        if prev_frame is None:
            prev_frame = blur
        else:
            diff = cv2.absdiff(prev_frame, blur)
            thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                if cv2.contourArea(cnt) > 1500:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(output, (x,y), (x+w,y+h), (0,0,255), 2)
                    cv2.putText(output, "Motion Detected",
                                (x,y-10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.6,
                                (0,0,255), 2)

            prev_frame = blur

    # ================= DOCUMENT SCANNER (IMPROVED) =================
    elif mode == "scanner":
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        for cnt in contours:
            if cv2.contourArea(cnt) > 5000:
                approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

                if len(approx) == 4:
                    pts = reorder_points(approx)

                    width, height = 500, 600
                    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
                    matrix = cv2.getPerspectiveTransform(
                        np.float32(pts.reshape(4,2)),
                        pts2)

                    warped = cv2.warpPerspective(frame, matrix, (width,height))
                    scanned = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
                    scanned = cv2.adaptiveThreshold(scanned,255,
                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                        cv2.THRESH_BINARY,11,2)

                    cv2.imshow("Scanned Output", scanned)
                    cv2.drawContours(output, [approx], -1, (0,255,0), 3)
                    break

    # ================= FACE MODE =================
    elif mode == "face":
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(output, (x,y), (x+w,y+h), (255,0,255), 2)
            cv2.putText(output, "Face", (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (255,0,255), 2)

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = output[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)

            smiles = smile_cascade.detectMultiScale(
                roi_gray, 1.8, 20)
            for (sx,sy,sw,sh) in smiles:
                cv2.rectangle(roi_color, (sx,sy),
                              (sx+sw,sy+sh), (0,255,255), 2)
                cv2.putText(output, "Smile Detected",
                            (x, y+h+20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0,255,255), 2)

    # ================= FPS + MODE TEXT =================
    fps = int(1/(time.time()-start_time + 0.001))

    cv2.putText(output, f"Mode: {mode}", (20,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255,255,0), 2)

    cv2.putText(output, f"FPS: {fps}", (20,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255,255,0), 2)

    cv2.imshow("OpenCV Vision Toolkit", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'): mode = "edges"
    elif key == ord('3'): mode = "color"
    elif key == ord('4'): mode = "motion"
    elif key == ord('5'): mode = "scanner"
    elif key == ord('6'): mode = "face"
    elif key == ord('q'): break

cap.release()
cv2.destroyAllWindows()