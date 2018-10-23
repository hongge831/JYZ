import os
import shutil
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

random.seed(2018)
jyzimg_src = 'E:/jyzdata/jyzsmallxmljson/images'
save_dir = 'E:/jyzdata/jyz_fake_img'
# img = Image.open(os.path.join(jyzimg_src,'1519892842807-jueyuanzi.jpg'))
imgname_list = os.listdir(jyzimg_src)
img_list = [os.path.join(jyzimg_src, x) for x in os.listdir(jyzimg_src)]
w_fix = 100
h_fix = 200
width = 0
height = 0
for idx, imgfile in tqdm(enumerate(img_list)):
    img = Image.open(imgfile)
    width, height = img.size
    for i in range(5):
        left_x = random.randint(0, width - w_fix)
        left_y = random.randint(0, height - h_fix)
        crop_img = img.crop((left_x, left_y, left_x + w_fix, left_y + h_fix))
        crop_img.save(os.path.join(save_dir, imgname_list[idx][:-4] + str(i) + '.jpg'))
