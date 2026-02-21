import cv2

def read():
    img = cv2.imread('aids.png')
    if img is None:
        print("Not loaded")
    else:
        print("Loaded")
        (h, w, c) = img.shape   # Note: shape gives (rows, cols, channels)
        print(f"Width: {w}, Height: {h}, No. of Color channels: {c}")

def gray():
    img = cv2.imread('aids.png')
    if img is None:
        print("Not loaded")
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray img", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def display():
    img = cv2.imread('aids.png')
    if img is None:
        print("Not loaded")
    else:
        cv2.imshow('Department Of AIDS', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def save():
    img = cv2.imread('aids.png')
    if img is None:
        print("Not loaded")
    else:
        cv2.imwrite('saved.jpg', img)
        print("Image saved as saved.jpg")

if __name__ == "__main__":
    while True:
        x = input("Choose option:\n1: Read\n2: GrayScale\n3: Display\n4: Save\nq: Quit\n--> ")

        if x == "1":
            read()
        elif x == "2":
            gray()
        elif x == "3":
            display()
        elif x == "4":
            save()
        elif x.lower() == "q":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")