# color-> gray 
import cv2
img=cv2.imread('flower.jpg',cv2.IMREAD_GRAYSCALE)
ret,thresh_img=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
cv2.imshow("Before thresholding",img)
cv2.imshow("After thresholding",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
40-0(black)
50-255(whitw)
>255 (white)
"""