import numpy as np
import cv2
import os

# load both image in 3 channel
test_beta = cv2.imread(
    "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_280.png",
    cv2.IMREAD_COLOR)
target = cv2.imread("/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png", cv2.IMREAD_COLOR)

# change both imagine to HSV

global_max = 0
global_max_path = ""

def template_matching(template_path):
    test_template = cv2.imread(template_path,cv2.IMREAD_COLOR)
    test_tempate_hsv = cv2.cvtColor(test_template, cv2.COLOR_BGR2HSV)

# Define color range anything but black
    lower_black = np.array([0, 0, 1])
    upper_black = np.array([255, 255, 255])

    mask = cv2.inRange(test_tempate_hsv, lower_black, upper_black)
    max_val_res = 0

    for x in range(30, 50):
        for y in range(30, 50):
            print("Processing path %s with size %d , %d" % (template_path, x , y))
        # print(x,y)
            target_depth = target.astype(np.uint8)
            target_greyscale = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
            target_greyscale_depth = target_greyscale.astype(np.uint8)

            template_resize = cv2.resize(test_template, (x, y))
            template_resize_depth = template_resize.astype(np.uint8)
            template_resize_greyscale = cv2.cvtColor(cv2.resize(test_template, (x, y)), cv2.COLOR_BGR2GRAY)
            template_resize_greyscale_depth = template_resize_greyscale.astype(np.uint8)

            mask_resize = cv2.resize(mask, (x, y))
            mask_resize_depth = mask_resize.astype(np.uint8)
            mask_resize_color = cv2.cvtColor(mask_resize, cv2.COLOR_GRAY2RGB)
            mask_resize_color_depth = mask_resize_color.astype(np.uint8)

            # print(target_depth.shape)
            # print(template_resize_depth.shape)
            # print(mask_resize_color_depth.shape)

            # cv2.TM_CCORR_NORMED or cv2.TM_SQDIFF
            res = cv2.matchTemplate(target_depth, template_resize_depth, cv2.TM_SQDIFF, mask=template_resize_depth)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            #print(max_val)
            if (max_val > max_val_res):
                max_val_res = max_val
                max_x_res = x
                max_y_res = y
            #if (max_val == max_val_res):
                #print("Match")
                # print("Size %d %d" % (x,y))
                #cv2.rectangle(target, max_loc, (max_loc[0] + x, max_loc[1] + y), (0, 255, 255), 2)
                # break
    #print("The result for file %s :" % test_template)
    #print(max_val_res, max_x_res, max_y_res)
    #cv2.imshow("ori", target)
    #cv2.imshow("template", cv2.resize(test_template, (max_x_res, max_y_res)).astype(np.uint8))
    #cv2.imshow("mask", cv2.resize(mask_resize_color_depth, (max_x_res, max_y_res)).astype(np.uint8))
    #cv2.waitKey(0)
    print("Globa_max is %f with template %s" % (global_max, global_max_path))
    return(max_val_res, max_x_res, max_y_res, template_path)

dir = "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out"
files = os.listdir(dir)

for file in files:
    png = os.path.join(dir,file)
    #print(png)
    (max_val_res, max_x_res, max_y_res, max_path) = template_matching(png)
    if (max_val_res > global_max):
        globa_max = max_val_res
        global_max_path = max_path

print("Globa_max is %f with template %s" % (global_max, global_max_path))


