import math
import numpy as np
import pandas as pd
import csv
from tqdm import tqdm


INFILE="may_24_data.csv"
OUTFILE1="test1.csv"
OUTFILE2="test2.csv"
OUTFILE3="test3.csv"
csv_file=open(INFILE)
IMAGE_HEIGHT=512
IMAGE_WIDTH=512
i=2

def calculate_90(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=ymin+y
    nw_ymax=h-xmin
    nw_xmin=ymin
    nw_ymin=nw_ymax-x
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax

def calculate_180(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-xmin
    nw_ymax=h-ymin
    nw_xmin=nw_xmax-x
    nw_ymin=nw_ymax-y
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax

def calculate_270(xmin,ymin,xmax,ymax,w,h):
    x=xmax-xmin
    y=ymax-ymin
    nw_xmax=w-ymin
    nw_ymax=xmin+x
    nw_xmin=nw_xmax-y
    nw_ymin=xmin
    return nw_xmin,nw_ymin,nw_xmax,nw_ymax

def write_data(list_data,OUTFILE):
    with open(OUTFILE,'a') as csvout:
        writer=csv.DictWriter(csvout,fieldnames=["image","xmin","ymin","xmax","ymax","label"])
        for data in list_data:
            writer.writerow(data) 

data_file=csv.DictReader(csv_file,delimiter=',')

list_data=[]

for row in tqdm(data_file):
    #print(row)
    list_data.append({
        "image" : row["image"],
        "xmin"  : row["xmin"],
        "ymin"  : row["ymin"],
        "xmax" 	: row["xmax"],
        "ymax"  : row["ymax"],
        "label" : row["label"]
    })

data1,data2,data3=list_data
print(list_data)

for dict_val in tqdm(list_data):
    dict_val["image"]="90"+dict_val["image"]
    nw_xmin,nw_ymin,nw_xmax,nw_ymax=calculate_90(float(dict_val["xmin"]),float(dict_val["ymin"]),float(dict_val["xmax"]),float(dict_val["ymax"]),IMAGE_WIDTH,IMAGE_HEIGHT)
    dict_val["xmin"]=str(nw_xmin)
    dict_val["ymin"]=str(nw_ymin)
    dict_val["xmax"]=str(nw_xmax)
    dict_val["ymax"]=str(nw_ymax)
write_data(list_data,OUTFILE1)
#print("After 1st change",list_data)


for dict_val in tqdm(list_data):
    dict_val["image"]="180"+dict_val["image"]
    nw_xmin,nw_ymin,nw_xmax,nw_ymax=calculate_180(float(dict_val["xmin"]),float(dict_val["ymin"]),float(dict_val["xmax"]),float(dict_val["ymax"]),IMAGE_WIDTH,IMAGE_HEIGHT)
    dict_val["xmin"]=str(nw_xmin)
    dict_val["ymin"]=str(nw_ymin)
    dict_val["xmax"]=str(nw_xmax)
    dict_val["ymax"]=str(nw_ymax)
write_data(list_data,OUTFILE2)
#print("After 2nd change",list_data)

for dict_val in tqdm(list_data):
    dict_val["image"]="270"+dict_val["image"]
    nw_xmin,nw_ymin,nw_xmax,nw_ymax=calculate_270(float(dict_val["xmin"]),float(dict_val["ymin"]),float(dict_val["xmax"]),float(dict_val["ymax"]),IMAGE_WIDTH,IMAGE_HEIGHT)
    dict_val["xmin"]=str(nw_xmin)
    dict_val["ymin"]=str(nw_ymin)
    dict_val["xmax"]=str(nw_xmax)
    dict_val["ymax"]=str(nw_ymax)
write_data(list_data,OUTFILE3)
    #print("After 3rd change",list_data)
