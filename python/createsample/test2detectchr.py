import numpy as np
import cv2
from PIL import ImageGrab
import time
#from Quartz.CoreGraphics import CGEventCreateMouseEvent

template = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/muskcard.png",0)
w,h = template.shape[::-1]

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,705,1251)))
    screen_gray = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screen_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    print("Took {}".format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow("window", cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



img1 = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/muskainselection.png")
img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

