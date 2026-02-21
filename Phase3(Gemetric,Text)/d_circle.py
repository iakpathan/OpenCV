import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Oops! Img not loaded")
else:
    center=(300,300)
    radius=50
    color=(0,0,255)
    thickness=4
    cv2.circle(img,center,radius,color,-1)
    cv2.imshow("Drawn circle",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

