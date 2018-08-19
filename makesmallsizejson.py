import json
import cv2
from PIL import Image
import os
from tqdm import tqdm
src = 'E:/jyzdata/jyzBig/'
desrc = 'E:/jyzdata/tets2/'
jsonList = [x for x in os.listdir(src) if x.endswith('json')]
for jsonFile in tqdm(jsonList):
    with open(src+jsonFile,'r') as f:
        jsonData = json.loads(f.read())
#         print(src+jsonFile[:-4]+'jpg')
#         imgOri = cv2.imread(src+jsonFile[:-4]+'jpg')
#         w,h,_ = imgOri.shape
        if(w>2000):
            for idx in range(len(jsonData['shapes'])):
                jsonData['shapes'][idx]['points'][0][0] = float(jsonData['shapes'][idx]['points'][0][0])//3
                jsonData['shapes'][idx]['points'][0][1] = float(jsonData['shapes'][idx]['points'][0][1])//3
                jsonData['shapes'][idx]['points'][1][0] = float(jsonData['shapes'][idx]['points'][1][0])//3
                jsonData['shapes'][idx]['points'][1][1] = float(jsonData['shapes'][idx]['points'][1][1])//3
                jsonData['shapes'][idx]['points'][2][0] = float(jsonData['shapes'][idx]['points'][2][0])//3
                jsonData['shapes'][idx]['points'][2][1] = float(jsonData['shapes'][idx]['points'][2][1])//3
                jsonData['shapes'][idx]['points'][3][0] = float(jsonData['shapes'][idx]['points'][3][0])//3
                jsonData['shapes'][idx]['points'][3][1] = float(jsonData['shapes'][idx]['points'][3][1])//3
#             imgNew = cv2.resize(imgOri,(h//3,w//3),interpolation=cv2.INTER_CUBIC)
#             print(imgNew.shape)
#         cv2.imwrite(desrc+jsonFile[:-4]+'jpg',imgNew)
        
    f.close()
    
    with open(desrc+jsonFile, 'w') as f:
        json.dump(jsonData,f)
    f.close()