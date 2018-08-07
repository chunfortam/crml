import numpy as np
import cv2
import matplotlib.pyplot as plt

test_tempate = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_286.png",cv2.IMREAD_UNCHANGED)
target = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png",1)

test_tempate_notalpha = np.where(test_tempate[:,:,3] != 0)
min_x = test_tempate.shape[0]
min_y = test_tempate.shape[1]
max_x = 0
max_y = 0
for pt in zip(*test_tempate_notalpha[::1]):
    if(pt[0] > max_x):
        max_x = pt[0]
    if(pt[0] < min_x):
        min_x = pt[0]
    if(pt[1] > max_y):
        max_y = pt[0]
    if(pt[1] < min_y):
        min_y = pt[0]

roi = test_tempate[min_x:max_x,min_y:max_y]

max_val_res = 0
max_x_res,max_y_res = 0,0
roi_resize_without_alpha =0
for x in range(30,35):
    for y in range(30,40):
        print(x,y)
        roi_resize = cv2.resize(roi,(x,y))
        roi_resize_without_alpha = roi_resize[:,:,:3]
        res = cv2.matchTemplate(target,roi_resize_without_alpha,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #print(max_val)
        if(max_val > max_val_res):
            max_val_res = max_val
            max_x_res = x
            max_y_res = y
        if(max_val > 0.6):
            #print("Match")
            #print("Size %d %d" % (x,y))
            cv2.rectangle(target, max_loc, (max_loc[0] + x, max_loc[1] + y), (0,255,255), 2)
            break

print(max_val_res,max_x_res,max_y_res)

cv2.imshow("ori",target)
cv2.imshow("roi",roi_resize)
cv2.imshow("ori3",roi_resize_without_alpha)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
