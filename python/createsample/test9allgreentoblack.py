import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

test_beta = cv2.imread(
    "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_280.png",
    cv2.IMREAD_COLOR)
target = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png", cv2.IMREAD_COLOR)
background = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/greenbackground.png", cv2.IMREAD_COLOR)
cloud = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/cloud.png", cv2.IMREAD_COLOR)
target_scr = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/target_screenshot.png",cv2.IMREAD_COLOR)

target_hsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
background_hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)
cloud_hsv = cv2.cvtColor(cloud,cv2.COLOR_BGR2HSV)
target_scr_hsv = cv2.cvtColor(target_scr,cv2.COLOR_BGR2HSV)

test_beta_gray = cv2.cvtColor(test_beta,cv2.COLOR_BGR2GRAY)
test_beta_hsv = cv2.cvtColor(test_beta,cv2.COLOR_BGR2HSV)

def findMinMaxHSV(image):
    maxH_image = np.amax(image[:,:,0])
    minH_image = np.amin(image[:,:,0])

    maxS_image = np.amax(image[:,:,1])
    minS_image = np.amin(image[:,:,1])

    maxV_image = np.amax(image[:,:,2])
    minV_image = np.amin(image[:,:,2])
    return (maxH_image,maxS_image,maxV_image),(minH_image,minS_image,minV_image)

(background_maxH,background_maxS,background_maxV) , (background_minH,background_minS,background_minV) = findMinMaxHSV(background_hsv)
print((background_maxH,background_maxS,background_maxV) , (background_minH,background_minS,background_minV))
def removeGreen(image,maxH,minH):
    coordinate = np.where((image[:,:,0] <= maxH) & (image[:,:,0] >= minH))
    for pt in zip(*coordinate[::1]):
        image[pt[0],pt[1]] = [0,0,0]
    return image
target_hsv_nogreen = removeGreen(target_hsv,background_maxH,background_minH)
cv2.imshow("target",target_hsv)

def matching(target, template):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(target,None)
    kp2, des2 = orb.detectAndCompute(template,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    img3 = cv2.drawMatches(target,kp1,template,kp2,matches[:5],None, flags=2)
    cv2.imshow("result",img3)
matching(target_hsv,test_beta_hsv)

cv2.waitKey(0)