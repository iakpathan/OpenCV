import cv2

img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    display=cv2.imshow('Department Of AIDS',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()