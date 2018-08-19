import os,sys
import os,sys
from PIL import Image
import cv2
import numpy as np
import os
from PIL import Image
from tqdm import tqdm
import matplotlib.pyplot as plt
##图像去除标记红框代码
src=''
dsr=''
for imgName in tqdm(os.listdir(dsr)):
    imgDir = dsr+imgName
    print(imgDir)
    img = cv2.imread(imgDir)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    h,w,c = img.shape
    mask = np.zeros((h,w,c), np.uint8)
    for i in range(0,h):
        for j in range(0,w):
            data = img[i][j]
            #uint8做减法会溢出，需转类型到int后再做减法
            if(int(data[0]) > 100 and abs(int(data[0])-int(data[1]))>50):
                #创建impainting模板，即图像中红色的区域，mask只需要单通道
                mask[i][j] +=255
                dstimg = cv2.inpaint(img,mask[:,:,0],20,cv2.INPAINT_TELEA)
                dstimg = cv2.cvtColor(dstimg,cv2.COLOR_BGR2RGB)
                cv2.imwrite(dsr2+imgName,dstimg)
print('Get rid of the red box is finished!')