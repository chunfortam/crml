import cv2
import numpy as np

img1 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/notroops7051251.png')
img2 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_074.png',-1)
img3 = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png')

print(img1.shape)
#crop imagine to just the object

y,x = img2[:,:,3].nonzero() # get the nonzero alpha coordinates
minx = np.min(x)
miny = np.min(y)
maxx = np.max(x)
maxy = np.max(y)

cropImg = img2[miny:maxy, minx:maxx]

img2_resize = cv2.resize(cropImg,(50,55))
#img2_resize = img2
#starting 209 is friendly (with blue)
rows,cols,_ = img2_resize.shape
roi = img1[650:650+rows, 450:450+cols]
img2gray = cv2.cvtColor(img2_resize,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
img2_fg_with_alpha = cv2.bitwise_and(img2_resize,img2_resize,mask = mask_inv)
img2_fg = img2_fg_with_alpha[:,:,:3]

print(img1_bg.shape)
print(img2_fg.shape)
dst = cv2.add(img1_bg,img2_fg)
img1[650:650+rows, 450:450+cols] = dst


cv2.imshow('mask',img1_bg)
cv2.imshow('img1',img1)
cv2.imshow('target',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()