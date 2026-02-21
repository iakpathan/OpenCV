import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray img",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()