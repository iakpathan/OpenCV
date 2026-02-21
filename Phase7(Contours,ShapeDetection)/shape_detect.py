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
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)  # slightly larger epsilon
    corners = len(approx)

    if corners == 3:
        shape = "Triangle"
    elif corners == 4:
        shape = "Rectangle"
    elif corners == 5:
        shape = "Pentagon"
    elif corners > 5:
        shape = "Circle"
    else:
        shape = "Unknown"

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)

    x, y = approx.ravel()[0], approx.ravel()[1]
    cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)  # bigger, red text

    
    cv2.imshow("Contors",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



