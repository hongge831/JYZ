# -- coding: utf-8 --
import os
import shutil
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
from PIL import Image
import numpy as np
import random
random.seed(2018)
src = '/Users/yefanfan/YFF/maps_cyclegan/test_latest/images'
real_A_src = '/Users/yefanfan/YFF/maps_cyclegan/test_latest/real_A'
fake_B_src = '/Users/yefanfan/YFF/maps_cyclegan/test_latest/fake_B'
diff_src = '/Users/yefanfan/YFF/maps_cyclegan/test_latest/diff'


def compute_diff(real_src, fake_src, diff_src, idx):
    ##读入图片，将图片转化成灰度图
    in_img = cv2.imread(real_src)
    out_img = cv2.imread(fake_src)
    in_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
    out_img = cv2.cvtColor(out_img, cv2.COLOR_BGR2GRAY)
    plt.imshow(in_img, cmap='gray')
    ##计算diff差
    diff_t = np.zeros(in_img.shape)
    diff = np.zeros(in_img.shape)
    w, h = in_img.shape
    for i in range(w):
        for j in range(h):
            if (in_img[i][j] < 90):
                #                 in_img[i][j] = 0
                out_img[i][j] = 0


#             if(in_img[i][j] ==0):
#                 d = 255
#             else:
#                 d = int(out_img[i][j]) - int(in_img[i][j])
#             diff[i][j] = abs(d) if d<0 else d
# 对图片进行归一化处理


#     maxv = np.max(diff)
#     diff2 = 255*diff//maxv
#     print(os.path.join(diff_src,str(idx)+'.jpg'))
#     cv2.imwrite(os.path.join(diff_src,str(idx)+'.jpg'),diff2)
#     plt.imshow(out_img, cmap = 'gray')


if __name__ == '__main__':
##打开输出图片，并转化成jpg格式，保存至对应的文件夹内
    for imgname in tqdm(os.listdir(src)):
        if(imgname.find('real_A')!=-1):
            img = Image.open(os.path.join(src,imgname))
            img.convert('RGB').save(os.path.join(real_A_src,imgname[:-4]+'.jpg'))
    #         shutil.copy(os.path.join(src,imgname),os.path.join(real_A_src,imgname))
        elif(imgname.find('fake_B')!=-1):
            img = Image.open(os.path.join(src,imgname))
            img.convert('RGB').save(os.path.join(fake_B_src,imgname[:-4]+'.jpg'))
    #         shutil.copy(os.path.join(src,imgname),os.path.join(fake_B_src,imgname))
        else:
            continue

    real_A_list = [os.path.join(real_A_src,x) for x in os.listdir(real_A_src)]
    fake_B_list = [os.path.join(fake_B_src,x) for x in os.listdir(fake_B_src)]
    real_A_list.sort()
    fake_B_list.sort()