import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    sliced=img[250:800,245:600]
    cv2.imshow("This is sliced img",sliced)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    