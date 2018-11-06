import numpy as np
import cv2
import keyboard
import time
import os
import re
from PIL import ImageGrab
def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

def findMaxNumber(path):
    files = os.listdir(path)
    files = sorted_aphanumeric(files)
    if len(files) != 0:
        file = files[-1]
        maxNumber = re.search(r'[a-z]*_([0-9]+).png',file).group(1)
        result =  int(maxNumber) + 1
        print(maxNumber)
        return result
    return 1
#472
def takeScreenShot(writing_path,char_name):
    number = findMaxNumber(writing_path)
    time_now = time.clock()
    image = np.array(ImageGrab.grab(bbox=(10,50,450,850)))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    file_name = char_name + "_" + str(number) + ".png"
    path = os.path.join(writing_path, file_name)
    print("ScreenShot captured at ", path)
    cv2.imwrite(path,image)
    print(time.clock() - time_now)
    return number + 1

while True:
    if keyboard.is_pressed('e'):
        writing_path = "D:\IdeaProjects\crml\python\musketter"
        maxNumber = takeScreenShot(writing_path,'musketter')
        print("Pressed e ", maxNumber)

    elif keyboard.is_pressed('w'):
        writing_path = r"D:\IdeaProjects\crml\python\nomusk"
        maxNumber = takeScreenShot(writing_path,'nomusk')
        print("Pressed w ", maxNumber)
    else:
        pass
