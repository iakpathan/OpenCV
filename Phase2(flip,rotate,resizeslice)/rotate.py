import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    (h,w,_)=img.shape
    center=(h//2,w//2)
    M=cv2.getRotationMatrix2D(center,90,1)
    rotated=cv2.warpAffine(img,M,(878,878))
    cv2.imshow("Original Img",img)
    cv2.imshow("Rotated Img",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()