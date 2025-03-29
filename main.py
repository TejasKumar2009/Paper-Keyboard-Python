# Import essential libraries 
import requests 
import cv2 
import numpy as np 
import imutils
import pyautogui

url = "http://192.168.1.34:8080/shot.jpg"

def find_red_dot(frame):
    height, width, channels = frame.shape
    print(height, width)

    red_pixels = []  # Store coordinates of red pixels

    for y_pixel in range(height):
        for x_pixel in range(width):
            b, g, r = frame[y_pixel, x_pixel]
            if r > 150 and g < 100 and b < 100:  # Simple red check
                red_pixels.append((x_pixel, y_pixel))

    if red_pixels:
        sum_x = 0
        sum_y = 0
        for x, y in red_pixels:
            sum_x += x
            sum_y += y
        if len(red_pixels) > 0: #prevent division by zero.
            cx = sum_x // len(red_pixels)
            cy = sum_y // len(red_pixels)

            # first row
            if (cx<91 and cy<94):
                pyautogui.press('`')
            elif (cx<91*2 and cy<94):
                pyautogui.press('1')
            elif (cx<91*3 and cy<94):
                pyautogui.press('2')
            elif (cx<91*4 and cy<94):
                pyautogui.press('3')
            elif (cx<91*5 and cy<94):
                pyautogui.press('4')
            elif (cx<91*6 and cy<94):
                pyautogui.press('5')
            elif (cx<91*7 and cy<94):
                pyautogui.press('6')
            elif (cx<91*8 and cy<94):
                pyautogui.press('7')
            elif (cx<91*9 and cy<94):
                pyautogui.press('8')
            elif (cx<91*10 and cy<94):
                pyautogui.press('9')
            elif (cx<91*11 and cy<94):
                pyautogui.press('10')

            # Second row    
            elif (cx<91 and cy<188):
                pyautogui.press('q')
            elif (cx<91*2 and cy<188):
                pyautogui.press('w')
            elif (cx<91*3 and cy<188):
                pyautogui.press('e')
            elif (cx<91*4 and cy<188):
                pyautogui.press('r')
            elif (cx<91*5 and cy<188):
                pyautogui.press('t')
            elif (cx<91*6 and cy<188):
                pyautogui.press('y')
            elif (cx<91*7 and cy<188):
                pyautogui.press('u')
            elif (cx<91*8 and cy<188):
                pyautogui.press('i')
            elif (cx<91*9 and cy<188):
                pyautogui.press('o')
            elif (cx<91*10 and cy<188):
                pyautogui.press('p')
            elif (cx<91*11 and cy<188):
                pyautogui.press('backspace')


            # Third row
            elif (cx<91 and cy<282):
                pyautogui.press('a')
            elif (cx<91*2 and cy<282):
                pyautogui.press('s')
            elif (cx<91*3 and cy<282):
                pyautogui.press('d')
            elif (cx<91*4 and cy<282):
                pyautogui.press('f')
            elif (cx<91*5 and cy<282):
                pyautogui.press('g')
            elif (cx<91*6 and cy<282):
                pyautogui.press('h')
            elif (cx<91*7 and cy<282):
                pyautogui.press('j')
            elif (cx<91*8 and cy<282):
                pyautogui.press('k')
            elif (cx<91*9 and cy<282):
                pyautogui.press('l')
            elif (cx<91*10 and cy<282):
                pyautogui.press('-')
            elif (cx<91*11 and cy<282):
                pyautogui.press('+')

            # Fourth row
            elif (cx<91 and cy<94*4):
                pyautogui.press('z')
            elif (cx<91*2 and cy<94*4):
                pyautogui.press('x')
            elif (cx<91*3 and cy<94*4):
                pyautogui.press('c')
            elif (cx<91*4 and cy<94*4):
                pyautogui.press('v')
            elif (cx<91*5 and cy<94*4):
                pyautogui.press('b')
            elif (cx<91*6 and cy<94*4):
                pyautogui.press('n')
            elif (cx<91*7 and cy<94*4):
                pyautogui.press('m')
            elif (cx<91*8 and cy<94*4):
                pyautogui.press('[')
            elif (cx<91*9 and cy<94*4):
                pyautogui.press(']')
            elif (cx<91*10 and cy<94*4):
                pyautogui.press('\\')
            elif (cx<91*11 and cy<94*4):
                pyautogui.press('enter')

            # Fifth row
            elif (cx<91 and cy<94*5):
                pyautogui.press('tab')
            elif (cx<91*2 and cy<94*5):
                pyautogui.press('capslock')
            elif (cx<91*3 and cy<94*5):
                pyautogui.press('scrolllock')
            elif (cx<91*4 and cy<94*5):
                pyautogui.press('esc')
            elif (cx<91*5 and cy<94*5):
                pyautogui.press('insert')
            elif (cx<91*6 and cy<94*5):
                pyautogui.press('delete')
            elif (cx<91*7 and cy<94*5):
                pyautogui.press('prtscr')
            elif (cx<91*8 and cy<94*5):
                pyautogui.press('playpause')
            elif (cx<91*9 and cy<94*5):
                pyautogui.press('pageup')
            elif (cx<91*10 and cy<94*5):
                pyautogui.press('pagedown')
            elif (cx<91*11 and cy<94*5):
                pyautogui.press('win')

            # Sixth row
            elif (cx<91 and cy<94*6):
                pyautogui.press('shift')
            elif (cx<91*2 and cy<94*6):
                pyautogui.press('ctrl')
            elif (cx<91*3 and cy<94*6):
                pyautogui.press('win')
            elif (cx<91*4 and cy<94*6):
                pyautogui.press('alt')
            elif (cx<91*5 and cy<94*6):
                pyautogui.press('space')
            elif (cx<91*6 and cy<94*6):
                pyautogui.press(',')
            elif (cx<91*7 and cy<94*6):
                pyautogui.press('.')
            elif (cx<91*8 and cy<94*6):
                pyautogui.press('up')
            elif (cx<91*9 and cy<94*6):
                pyautogui.press('down')
            elif (cx<91*10 and cy<94*6):
                pyautogui.press('left')
            elif (cx<91*11 and cy<94*6):
                pyautogui.press('right')

            return cx, cy
        else:
            return -1, -1 #if no red pixel was found.
    else:
        return -1, -1

cap = cv2.VideoCapture(0)

while True:
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img) 

    red_x, red_y = find_red_dot(img)

    if red_x != -1 and red_y != -1:
        cv2.circle(img, (red_x, red_y), 5, (0, 255, 0), -1)
        print(f"Red dot position: ({red_x}, {red_y})")
    else:
        print("Red dot not found in this frame.")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()