import cv2

def draw_circle(img):
    x = int(input("Enter center x: "))
    y = int(input("Enter center y: "))
    r = int(input("Enter radius: "))
    color = (0, 0, 255)  # red
    thickness = int(input("Enter thickness (-1 for filled): "))
    cv2.circle(img, (x, y), r, color, thickness)
    return img

def draw_line(img):
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    color = (0, 255, 0)  # green
    thickness = int(input("Enter thickness: "))
    cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    return img

def draw_rectangle(img):
    x1 = int(input("Enter top-left x: "))
    y1 = int(input("Enter top-left y: "))
    x2 = int(input("Enter bottom-right x: "))
    y2 = int(input("Enter bottom-right y: "))
    color = (255, 0, 0)  # blue
    thickness = int(input("Enter thickness (-1 for filled): "))
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
    return img

def draw_text(img):
    text = input("Enter text: ")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    color = (0, 0, 255)  # red
    font = cv2.FONT_HERSHEY_COMPLEX
    scale = float(input("Enter font scale (e.g. 1.0): "))
    thickness = int(input("Enter thickness: "))
    cv2.putText(img, text, (x, y), font, scale, color, thickness)
    return img

if __name__ == "__main__":
    path = input("Enter image file path: ")
    img = cv2.imread(path)

    if img is None:
        print("Oops! Image not loaded. Check path.")
    else:
        while True:
            print("\nOptions:")
            print("1: Circle")
            print("2: Line")
            print("3: Rectangle")
            print("4: Text")
            print("s: Save")
            print("q: Quit")

            choice = input("Choose option: ")

            if choice == "1":
                img = draw_circle(img)
            elif choice == "2":
                img = draw_line(img)
            elif choice == "3":
                img = draw_rectangle(img)
            elif choice == "4":
                img = draw_text(img)
            elif choice.lower() == "s":
                out = input("Enter filename to save (e.g. output.jpg): ")
                cv2.imwrite(out, img)
                print(f"Image saved as {out}")
            elif choice.lower() == "q":
                break
            else:
                print("Invalid choice.")

            cv2.imshow("Edited Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()