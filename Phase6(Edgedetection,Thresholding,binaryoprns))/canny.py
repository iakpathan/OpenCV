import cv2
img=cv2.imread('flower.jpg',cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(img,100,300)
cv2.imshow("Before canny",img)
cv2.imshow("After canny",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()