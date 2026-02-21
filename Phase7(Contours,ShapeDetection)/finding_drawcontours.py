import cv2
img=cv2.imread('triangle.jpg')
if img is None:
    print("Img not loaded")
else:
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    #find contors
    contours,heirarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,-1,(0,255,0),3)
    cv2.imshow("Contors",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



