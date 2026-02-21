import cv2
img=cv2.imread('aids.png')
if img is None:
    print("Not loaded")
else:
    print("Loaded")
    (w,h,c)=img.shape
    print(f"Width :{w}, Height:{h},No.of Color channels:{c}")