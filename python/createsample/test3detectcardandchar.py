#(65, 78) size of bbox
#left to right
#(119, 729)
#(206, 732)
#(283, 734)
#(371, 731)

import numpy as np
import cv2
#from PIL import ImageGrab
#import win32api,win32con
import os
import datetime

templates = np.array([])
dir = r"D:\IdeaProjects\crml\picture\template"
filenames = os.listdir(dir)
for filename in filenames:
    path = os.path.join(dir, filename)
    pic = cv2.imread(path)
    print(pic.shape)
    templates = np.append(templates,pic)

#temp = cv2.imread("D:\IdeaProjects\crml\picture\windowtemplatetest.png")
#temp = temp[0:2,0:2]
#cv2.imwrite(os.path.join(dir, "white.png"),temp)
print(templates.shape)

while(True):
   img1 = cv2.imread("D:\IdeaProjects\crml\picture\windowtemplatetest.png")
   boxs = []
   #cards = []
   gap = 85

   for i in range(0,4):
       boxs.append(((100 + gap * i,705),(105 + gap * i, 715)))
   #boxs = [(100,705),(185,705),(330,705),(330,705)]
   #cards = [(105, 715),(185, 715),(283, 715),(371, 715)]

   boxw = 70
   boxh = 80

   cardw = 50
   cardh = 60
   testboxroi = []
   testcardroi = []

   for box,card in boxs:
       temp_template = []
       testboxroi = img1[box[1]:box[1]+boxh,box[0]:box[0]+boxw]
       testboxroi_grey = cv2.cvtColor(testboxroi,cv2.COLOR_BGR2GRAY)
       for template in templates:
           print(template.shape)
           res = cv2.matchTemplate(testboxroi_grey,template,cv2.TM_CCOEFF_NORMED)
           min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
           if max_val > 0.9:
               print("it is a match, not template needed")
               break
           else:
               print("No template found, writing a new one")
               testcardroi = img1[card[1]:card[1]+cardh,card[0]:card[0]+cardw]
               name = os.path.join(dir, datetime.datetime.now())
               cv2.imwrite(name,testcardroi)
       templates = np.append(templates,temp_template)

       #cv2.rectangle(img1, box, (box[0] + boxw, box[1] + boxh), (0,255,255), 2)
   #for card in cards:
       #cv2.rectangle(img1, card, (card[0] + cardw, card[1] + cardh), (255,0,255), 2)
       #testcardroi = img1[card[1]:card[1]+cardh,card[0]:card[0]+cardw]
   #testcardroi = cv2.cvtColor(testcardroi,cv2.COLOR_BGR2GRAY)


   #cv2.rectangle(testboxroi, max_loc, (max_loc[0] + cardw, max_loc[1] + cardh), (0,255,255), 2)
   #print(min_val,max_val,min_loc,max_loc)

   cv2.imshow("window",img1)
   if cv2.waitKey(25) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break