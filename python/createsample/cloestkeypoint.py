import numpy as np
import cv2
import matplotlib.pyplot as plt


target = cv2.imread('/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png',cv2.IMREAD_GRAYSCALE)
#img1 = cv2.imread('/Users/ctam/IdeaProjects/opencvtutorial/bookpage.jpg',0)
file = "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/gameplaywithchr.png"
#file = "/Users/ctam/Downloads/Old_IdeaProjects/crml/picture/chr_musketeer_out/chr_musketeer_sprite_286.png"
test_template = cv2.imread(file,cv2.IMREAD_COLOR )
test_template_gray = cv2.imread(file,cv2.IMREAD_GRAYSCALE )

test_template_gray = np.float32(test_template_gray)
target = np.float32(target)

corners = cv2.goodFeaturesToTrack(test_template_gray,12,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(test_template,(x,y),3,255,-1)

plt.imshow(test_template),plt.show()
