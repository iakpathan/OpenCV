import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    flipped_hori=cv2.flip(img,1)
    flipped_vert=cv2.flip(img,0)
    flipped_both=cv2.flip(img,-1)
    cv2.imshow("original",img)
    cv2.imshow("horizontal flip",flipped_hori)
    cv2.imshow("vertical flip",flipped_vert)
    cv2.imshow("Both",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    