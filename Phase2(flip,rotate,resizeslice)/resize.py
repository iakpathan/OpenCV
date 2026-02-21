import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    resized=cv2.resize(img,(300,300))
    print(f"Before resizing:{img.shape}")
    print(f"After resizing:{resized.shape}")
    cv2.imshow("After resizing",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    