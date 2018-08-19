#绝缘子图像预处理代码二：去除图像中的红色标记框，
#并根据图像的长宽比resize图像大小至长宽均为2的N次方
#代码时间：2018年8月17日下午
#作者YFF

##为了方便使用，将resize和去除红框分开处理
import os,sys
from PIL import Image
import cv2
import numpy as np
import os
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt

#图像resize处理
src ='E:/jyzdata/JYZvideo/video/images/aligned/dangeboli/'
dsr = 'E:/jyzdata/JYZvideo/video/images/aligned/dangeboliresize/'
dsr2 = 'E:/jyzdata/aligned/PSNormal_resize_nored/'
fileList = [x for x in os.listdir(src)]
widthList = []
heightList = []
rateList = []
preList = [128,256,512,1024]
print('Total number of images are %d' %len(fileList))
print('====================================')
for imgName in tqdm(fileList):
    img = Image.open(src+imgName)
    w,h = img.size  
    rate = round(w/h)
    widthList.append(w)
    heightList.append(h)
    rateList.append(rate)
    print('width = %d, heigth = %d, rate = %d' %(w,h,round(w/h)))
    ##按照高度对图片进行分类，将高度resize到[128，256，512，1024]区间，然后根据长宽比例进行宽度的resize
    if(h/256 > 0):
        imgNew = img.resize((rate*256,256))
    else:
        imgNew = img.resize((rate*128,128))
    newW,newH = imgNew.size
    if(rate > 6):
        imgNew1 = imgNew.crop((0, 0, newW/2,newH))
        imgNew2 = imgNew.crop((newW/2, 0, newW,newH))
        imgNew1.save(dsr+imgName[:-4]+'_l.jpg')
        imgNew2.save(dsr+imgName[:-4]+'_r.jpg')
    else:
        imgNew.save(dsr+imgName)
    
print('maxW = %d minW = %d maxH = %d minH = %d'%(max(widthList),min(widthList),max(heightList),min(heightList)))
print('Resize operation finished!')