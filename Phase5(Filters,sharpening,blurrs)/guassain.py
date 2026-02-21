import cv2
img=cv2.imread('hogwarts.jpg')
blurred=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Original img",img)
cv2.imshow("Blurred img",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
