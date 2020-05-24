import math
import numpy as np
import pandas as pd
import csv
from tqdm import tqdm

def calculate_180(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-xmin
    nw_ymax=h-ymin
    nw_xmin=nw_xmax-x
    nw_ymin=nw_ymax-y
    #print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax



def calculate_270(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-ymin
    nw_ymax=xmin+x
    nw_xmin=nw_xmax-y
    nw_ymin=xmin

    return nw_xmin,nw_ymin,nw_xmax,nw_ymax
    #print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)

def calculate_90(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=ymin+y
    nw_ymax=h-xmin
    nw_xmin=ymin
    nw_ymin=nw_ymax-x
    #print("xmin",nw_xmin,"ymin",nw_ymin,"xmax",nw_xmax,"ymax",nw_ymax)
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax

INFILE="indata.csv"
'''
csv_read=pd.read_csv("indata.csv")
images=csv_read['image']
labels_list = csv_read['label'].tolist()
xmin=csv_read['xmin']
xmax=csv_read['xmax']
ymin=csv_read['ymin']
ymax=csv_read['ymax']

#print(images,labels_list)
#print(xmin+500)
#rotate_180=calculate_180(248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956,512,512)
#print(type(rotate_180))
#print("orginial 248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956")
#calculate_180(248.07339449541286,106.86238532110093,445.35779816513764,266.56880733944956,512,512)
cal_val=calculate_90(xmin,ymin,xmax,ymax,512,512)
print(type(cal_val))
print(type(images))
#calculate_180(243.9633027522936,247.7798165137615,403.66972477064223,443.88990825688074,512,512)
'''

csv_file=open(INFILE)

data_file=csv.DictReader(csv_file,fieldnames=["image","xmin","ymin","xmax","ymax","label"])

list_data=[]
list_label=[]

for row in tqdm(data_file):
    list_data.append({
        "image" : row["image"],
        "xmin"  : row["xmin"],
        "ymin"  : row["ymin"],
        "xmax" 	: row["xmax"],
        "ymax"  : row["ymax"],
        "label" : row["label"]
    })

print(type(list_data))
for dict_val in list_data:
    dict_val["image"]="90"+dict_val["image"]
    nw_xmin,nw_ymin,nw_xmax,nw_ymax=calculate_90(float(dict_val["xmin"]),float(dict_val["ymin"]),float(dict_val["xmax"]),float(dict_val["ymax"]),512,512)
    dict_val["xmin"]=str(nw_xmin)
    dict_val["ymin"]=str(nw_ymin)
    dict_val["xmax"]=str(nw_xmax)
    dict_val["ymax"]=str(nw_ymax)
    print(dict_val["image"])

print((list_data))