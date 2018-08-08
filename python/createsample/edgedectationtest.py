import cv2
import numpy as np

img1 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/notroops7051251.png')
img2 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_074.png',-1)
img3 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_280.png', cv2.IMREAD_COLOR)
img4 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png', cv2.IMREAD_COLOR)
img3 = cv2.resize(img3,(70,80))
y,x = img2[:,:,3].nonzero() # get the nonzero alpha coordinates
minx = np.min(x)
miny = np.min(y)
maxx = np.max(x)
maxy = np.max(y)

cropImg = img2[miny:maxy, minx:maxx]
cropImg = cv2.resize(cropImg,(50,58))
cv2.imwrite("cropped.png", cropImg)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.waitKey(0)