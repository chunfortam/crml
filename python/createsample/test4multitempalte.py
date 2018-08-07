import numpy as np
import cv2
from PIL import ImageGrab
import time
import os
#from Quartz.CoreGraphics import CGEventCreateMouseEvent

files = os.listdir("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out")
images = []
for file in files:
    path = os.path.join("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out",file)
    #print(path)
    images.append(cv2.imread(path,cv2.IMREAD_UNCHANGED))

test_tempate = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_286.png",-1)
target = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png",-1)

w,h,a = test_tempate.shape[::-1]

threshold = 0.5

x = 49
y = 49
found = False

while(not found):
    print(x,y)
    x += 1
    y += 1
    resize_tempate = cv2.resize(test_tempate,(x,y))
    res = cv2.matchTemplate(resize_tempate,target,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if(max_val > 0.5):
        print("Match")
        print("Size %d %d" % (x,y))
        cv2.rectangle(target, max_loc, (max_loc[0] + x, max_loc[1] + y), (0,255,255), 2)
        found = True


cv2.imshow('target',test_tempate)
cv2.imshow("after target",target)
cv2.waitKey(0)

