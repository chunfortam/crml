import cv2
import numpy as np

img1 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/notroops7051251.png')
img2 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_074.png',-1)

y,x = img2[:,:,3].nonzero() # get the nonzero alpha coordinates
minx = np.min(x)
miny = np.min(y)
maxx = np.max(x)
maxy = np.max(y)

cropImg = img2[miny:maxy, minx:maxx]
cropImg = cv2.resize(cropImg,(50,58))
cv2.imwrite("cropped.png", cropImg)
cv2.imshow("cropped", cropImg)
cv2.waitKey(0)