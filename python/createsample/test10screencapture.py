import numpy as np
import pyautogui
import cv2
import keyboard
import time
import os
import re

def findMaxNumber():
    files = os.listdir("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/screenshot")
    file = files[-1]
    maxNumber = re.search('musketeer_([0-9]+).png',file).group(1)
    return int(maxNumber) + 1
def takeScreenShot(number):
    time_now = time.clock()
    image = pyautogui.screenshot()
    image = np.array(image)
    #705:1251
    roi = image[:1251,:705]
    file_name = "musketeer_" + str(number) + ".png"
    path = os.path.join("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/screenshot", file_name)
    print("ScreenShot captured at ", path)
    cv2.imwrite(path,roi)
    print(time.clock() - time_now)
    return number + 1


maxNumber = findMaxNumber()
while True:
    if keyboard.is_pressed('e'):
        print("Pressed e ", maxNumber)
        maxNumber = takeScreenShot(maxNumber)
    else:
        pass

