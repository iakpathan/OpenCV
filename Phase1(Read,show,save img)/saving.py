import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    saved=cv2.imwrite('saved.jpg',img)