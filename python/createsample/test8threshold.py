import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# load both image in 3 channel
test_beta = cv2.imread(
    "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_280.png",
    cv2.IMREAD_COLOR)
target = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png", cv2.IMREAD_COLOR)
background = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/greenbackground.png", cv2.IMREAD_COLOR)
cloud = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/cloud.png", cv2.IMREAD_COLOR)
target_scr = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/target_screenshot.png",cv2.IMREAD_COLOR)

target_hsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
print(target_hsv[713,403])
print(target_hsv[740,365])
background_hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)
cloud_hsv = cv2.cvtColor(cloud,cv2.COLOR_BGR2HSV)
target_scr_hsv = cv2.cvtColor(target_scr,cv2.COLOR_BGR2HSV)

test_beta_gray = cv2.cvtColor(test_beta,cv2.COLOR_BGR2GRAY)




def findMinMaxHSV(image):
    maxH_image = np.amax(image[:,:,0])
    minH_image = np.amin(image[:,:,0])

    maxS_image = np.amax(image[:,:,1])
    minS_image = np.amin(image[:,:,1])

    maxV_image = np.amax(image[:,:,2])
    minV_image = np.amin(image[:,:,2])

    print("return", (maxH_image,maxS_image,maxV_image),(minH_image,minS_image,minV_image))
    return (maxH_image,maxS_image,maxV_image),(minH_image,minS_image,minV_image)

(target_scr_maxH, target_scr_maxS, target_scr_maxV),(target_scr_minH,target_scr_minS,target_scr_minV) = findMinMaxHSV(target_scr_hsv)
(cloud_maxH,cloud_maxS,cloud_maxV) , (cloud_minH,cloud_minS,cloud_minV) = findMinMaxHSV(cloud_hsv)
(background_maxH,background_maxS,background_maxV) , (background_minH,background_minS,background_minV) = findMinMaxHSV(background_hsv)

#print((background_maxH,background_maxS,background_maxV) , (background_minH,background_minS,background_minV))
lower_green = np.array([background_minH, cloud_minS, cloud_minV])
upper_green = np.array([background_maxH, background_maxS, background_maxV])

print(lower_green)
print(upper_green)

mask = cv2.inRange(target_hsv, lower_green, upper_green)
mask = 255 - mask

res = cv2.bitwise_and(target,target, mask= mask)
res_gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#cv2.imshow('res',res)
#cv2.imshow('res_gray',res_gray)
cv2.imshow('mask',mask)

def matching(target, template):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(target,None)
    kp2, des2 = orb.detectAndCompute(template,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3 = cv2.drawMatches(target,kp1,template,kp2,matches[:5],None, flags=2)
    plt.imshow(img3)
    #plt.show()

matching(res_gray,test_beta_gray)
#cv2.imshow("test_beta", test_beta)
cv2.imshow("target", target)
#cv2.imshow("background", background)
cv2.waitKey(0)