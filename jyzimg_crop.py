# -- coding: utf-8 --
#这个脚本是用来处理从一串绝缘子中截取单个绝缘子片的
#作者：叶帆帆
#创建时间，2018年10月19日
import os
from PIL import Image
import xml.dom.minidom
import numpy as np
from tqdm import tqdm
import shutil

ImgPath = '/Volumes/Seagate Backup Plus Drive/aligned_noPS/test/classone'
AnnoPath = '/Volumes/Seagate Backup Plus Drive/aligned_noPS/test/xml_classone'
ProcessedPath = '/Volumes/Seagate Backup Plus Drive/aligned_noPS/classone_crop'

if __name__ == '__main__':
    ##如果保存图片的目录不存在就创建
    if not os.path.exists(ProcessedPath):
        os.makedirs(ProcessedPath)
    imagelist = os.listdir(ImgPath)
    ##按照图片列表进行遍历
    for image in tqdm(imagelist):
        #     print(image)
        img_pre, ext = os.path.splitext(image)
        imgfile = os.path.join(ImgPath, image)
        xmlfile = os.path.join(AnnoPath, img_pre + '.xml')
        # print(xmlfile)
        ##判断该图片是否存在对应的xml文件，如果不存在就跳过
        if not os.path.exists(xmlfile):
            continue
        DomTree = xml.dom.minidom.parse(xmlfile)
        annotation = DomTree.documentElement
        filenameList = annotation.getElementsByTagName('filename')
        filename = filenameList[0].childNodes[0].data
        objectlist = annotation.getElementsByTagName('object')
        ##定义一个列表，存储每个目标的边框信息
        cropboxes = []
        for obj in objectlist:
            namelist = obj.getElementsByTagName('name')
            objectname = namelist[0].childNodes[0].data
            bndbox = obj.getElementsByTagName('bndbox')
            ##获取点的坐标
            for box in bndbox:
                x1_list = box.getElementsByTagName('xmin')
                x1 = int(x1_list[0].childNodes[0].data)
                y1_list = box.getElementsByTagName('ymin')
                y1 = int(y1_list[0].childNodes[0].data)
                x2_list = box.getElementsByTagName('xmax')
                x2 = int(x2_list[0].childNodes[0].data)
                y2_list = box.getElementsByTagName('ymax')
                y2 = int(y2_list[0].childNodes[0].data)
                w = x2 - x1
                h = y2 - y1
            box_cor = np.array([x1, y1, x2, y2])
            cropboxes.append(box_cor)
        ##打开图片进行裁剪操作
        current_img = Image.open(imgfile)
        width, height = current_img.size
        # 定义目标index
        idx = 0
        for cropbox in cropboxes:
            # print 'cropbox:',cropbox
            minX = max(0, cropbox[0])
            minY = max(0, cropbox[1])
            maxX = min(cropbox[2], width)
            maxY = min(cropbox[3], height)
            # print(minX, minY, maxX, maxY)
            cropbox = (minX, minY, maxX, maxY)
            cropedimg = current_img.crop(cropbox)
            cropedimg.save(ProcessedPath + '/' + img_pre + '_' + str(idx) + '.jpg')
            idx += 1
