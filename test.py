import cv2
import pyautogui
from PIL import Image
import pytesseract

windowName = "KPMG"
pyautogui.screenshot("tmp.png")
cv2.namedWindow(windowName)
img = cv2.imread("tmp.png")

# true if mouse is pressed
drawing = False

# if True, draw rectangle. Press 'm' to toggle to curve
mode = True 
(ix, iy) = (-1, -1)

def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix, iy) = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img = cv2.imread("tmp.png")
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 3)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ex, ey = x, y
        cv2.rectangle(img, (ix, iy), (ex, ey), (0, 255, 0), 3)
        roi = img[iy:ey, ix:ex]
        cv2.imwrite("roi.jpg",roi)
        text = pytesseract.image_to_string(Image.open("roi.jpg"))
        print(text)


cv2.setMouseCallback(windowName, draw_shape)

def main():
    global img

    while(True):
        cv2.imshow(windowName, img)
        
        k = cv2.waitKey(2)
        if k == ord('m') or k == ord('M'):
            img = cv2.imread("2.jpg")
        elif k == 27:
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()