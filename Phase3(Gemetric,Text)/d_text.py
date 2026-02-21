import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Oops! Img not loaded")
else:
    text="Dept. Of. AI&DS"
    color=(0,0,255)
    pt1=(60,350)
    thickness=4
    font=cv2.FONT_HERSHEY_COMPLEX
    fontscale=1.2
    cv2.putText(img,text,pt1,font,fontscale,color,thickness)
    cv2.imshow("Written Text",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

