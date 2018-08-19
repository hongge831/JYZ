import cv2
from math import *
import numpy as np

img = cv2.imread("D:/1.jpg")


height, width = img.shape[:2]

degree = 15
# 旋转后的尺寸
heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))  # 这个公式参考之前内容
widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)

matRotation[0, 2] += (widthNew - width) / 2  # 因为旋转之后,坐标系原点是新图像的左上角,所以需要根据原图做转化
matRotation[1, 2] += (heightNew - height) / 2

imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))

cv2.imshow("img", img)
cv2.imshow("imgRotation", imgRotation)
cv2.waitKey(0)