'''
1)draw line ii)detect faces eyes etc and draw circle or any shape
iii)Analyse ->saving specific time of that frame etc
all these are used in AI (Self driving cars)
'''
import cv2
camera=cv2.VideoCapture(0)
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_heigth=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec=cv2.VideoWriter_fourcc(*'XVID')
recorder=cv2.VideoWriter("captured_video.avi",codec,20,(frame_width,frame_heigth))
while True:
    success,frame=camera.read()
    if not success:
        break
    recorder.write(frame)
    cv2.imshow("Recording Live",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
