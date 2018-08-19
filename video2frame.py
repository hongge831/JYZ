import cv2
import os
from tqdm import tqdm
src = 'E:/jyzdata/JYZvideo/video/'
drc = 'E:/jyzdata/JYZvideo/video/images/'
videoList = [x for x in os.listdir('E:/jyzdata/JYZvideo/video') if x.endswith('mp4')]
for videoName in tqdm(videoList):
    vc = cv2.VideoCapture(src + videoName) #读入视频文件
    c=1 
    if vc.isOpened(): #判断是否正常打开
        rval , frame = vc.read()
    else:
        rval = False 
    timeF = 20  #视频帧计数间隔频率

    while rval:   #循环读取视频帧
        rval, frame = vc.read()
        if(c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite('E:/jyzdata/JYZvideo/video/images/'+videoName+'_'+str(c) + '.jpg',frame) #存储为图像
        c = c + 1
        cv2.waitKey(1)
    vc.release()