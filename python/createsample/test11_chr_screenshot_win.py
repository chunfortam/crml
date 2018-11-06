import numpy as np
import cv2
import os
import re
from PIL import ImageGrab

def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

def onclick(event,x,y,flags,param):
    global maxNumber
    if event == cv2.EVENT_LBUTTONDOWN:
        print(maxNumber)
        maxNumber = takeScreenShot(maxNumber,x,y)
        return maxNumber

def findMaxNumber(path):
    files = os.listdir(path)
    files = sorted_aphanumeric(files)
    if len(files) != 0:
        file = files[-1]
        maxNumber = re.search(r'[a-z]*_([0-9]+).png',file).group(1)
        result = int(maxNumber) + 1
        print(maxNumber)
        return result
    return 1
def takeScreenShot(number,mouseX, mouseY):
    global screen
    print(mouseX,mouseY)
    width = 60
    height = 60
    roi = screen[mouseY:mouseY+width,mouseX:mouseX+height]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    #file_name = "musketeer_" + str(number) + ".png"
    file_name = "babydragon_" + str(number) + ".png"
    global path
    write_path = os.path.join(path, file_name)
    print("ScreenShot captured at ", write_path)
    cv2.imwrite(write_path,roi)
    return number + 1

def screen_record(path):
    global maxNumber
    maxNumber = findMaxNumber(path)
    cv2.namedWindow("screen")
    cv2.setMouseCallback("screen",onclick)
    while(True):
        printscreen = np.array(ImageGrab.grab(bbox=(10,50,450,850)))
        global screen
        screen = printscreen
        cv2.imshow('screen',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


global path
#path = "D:\IdeaProjects\crml\picture\chr_musk_screenshot"
#path = "D:\IdeaProjects\crml\picture\chr_knight_screenshot"
path = "D:\IdeaProjects\crml\picture\chr_babydragon_screenshot"

create_dir(path)
screen_record(path)