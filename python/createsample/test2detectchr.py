import numpy as np
import cv2
from PIL import ImageGrab
import time

template = cv2.imread("D:\IdeaProjects\crml\picture\windowmusckcard.png",0)
w,h = template.shape[::-1]
#print("template size %d %d" % (w,h))

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,450,850)))
    screen_gray = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
    #screen = cv2.imread("D:\IdeaProjects\crml\picture\windowtemplatetest.png")
    #screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screen_gray,template,cv2.TM_CCOEFF_NORMED)
    #cv2.imshow("template",template)
    threshold = 0.8
    loc = np.where(res >= threshold)
    if len(loc[0]) != 0:
        print("A Match")
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    print("Took {}".format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow("window", cv2.cvtColor(screen,cv2.COLOR_BGR2RGB))
    ##cv2.imshow("window",screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break