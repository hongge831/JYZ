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
%matplotlib inline

#图像resize处理
src ='E:/jyzdata/aligned/PSNormal/'
dsr = 'E:/jyzdata/aligned/PSNormal_resize/'
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

##图像去除标记红框代码
for imgName in tqdm(os.listdir(dsr2)):
    imgDir = dsr2+imgName
    img = cv2.imread(imgDir)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w,c = img.shape
    mask = np.zeros((h,w,c), np.uint8)
    for i in h:
        for j in w:
            data = img[i][j]
            #uint8做减法会溢出，需转类型到int后再做减法
            if(int(data[0]) > 100 and abs(int(data[0])-int(data[1]))>50):
                #创建impainting模板，即图像中红色的区域，mask只需要单通道
                mask[i][j] +=255
                dstimg = cv2.inpaint(img,mask[:,:,0],20,cv2.INPAINT_TELEA)
                cv2.imwrite(dsr2+imgName,dstimg)
print('Get rid of the red box is finished!')
                
                
                
                
            
    
    


