@author: pyada
"""

import json
import pandas as pd
import csv



file_path= " path to "predictions.json" file
confidence_threshold=0.50           #Set confidence threshold value above which you want to extract bounding box coordinates.

def read_josn(filepath):
  with open(filepath,'r')as f:
    data=json.load(f)
  return(data)

data=read_josn(file_path)
df=pd.DataFrame(data)
cf=df['confidence']
cf=pd.to_numeric(cf)
file_id=df['file_id']
#file_id=pd.to_numeric(file_id)
bbox=df['bbox']

bboxes=[]
f_id=[]
for i in range(len(cf)):
    if cf[i] >=confidence_threshold:
        bboxes.append(bbox[i])
        f_id.append(file_id[i])
vc_num=len(bboxes)
print("There are total number of detected volunteer cotton plants=",vc_num)

header=['file_id','bbox_coordinates']       
with open("bbox_coordinates.csv", 'w') as file: 
    dw = csv.DictWriter(file, delimiter=',',  
                        fieldnames=header) 
    dw.writeheader()
    for j in range(len(bboxes)):
        file.write("{},{}\n".format(f_id[j], bboxes[j]))
file.close()            
    
