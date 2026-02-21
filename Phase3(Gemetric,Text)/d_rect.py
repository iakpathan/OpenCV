import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Oops! Img not loaded")
else:
    pt1=(250,300)
    pt2=(60,240)
    color=(0,0,255)
    thickness=4
    cv2.rectangle(img,pt1,pt2,color,thickness)
    cv2.imshow("Drawn line",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

