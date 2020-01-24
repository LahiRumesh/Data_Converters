import csv
from tqdm import tqdm

input_file = csv.DictReader(open("input.csv"))
output_file="out1.csv"
list_data=[]
LABEL_0='label0'
LABEL_1='label1'
LABEL_2='label2'
LABEL_3='label3'
LABEL_4='label4'
LABEL_5='label5'
LABEL_6='label6'
LABEL_7='label7'
LABEL_8='label8'
LABEL_9='label9'

for row in tqdm(input_file):
    label=int(row["label"])
    if label==0:
        label=LABEL_0
    elif label==1:
        label=LABEL_1
    elif label==2:
        label=LABEL_2
    elif label==3:
        label=LABEL_3
    elif label==4:
        label=LABEL_4
    elif label==5:
        label=LABEL_5
    elif label==6:
        label=LABEL_6
    elif label==7:
        label=LABEL_7
    elif label==8:
        label=LABEL_8
    elif label==9:
        label=LABEL_9

    list_data.append({
        "image" : row["image"],
        "xmin"  : row["xmin"],
        "ymin"  : row["ymin"],
        "xmax" 	: row["xmax"],
        "ymax"  : row["ymax"],
        "label" : label
    })



with open(output_file,'w') as csvout:
    writer=csv.DictWriter(csvout,fieldnames=["image","xmin","ymin","xmax","ymax","label"])
    for data in list_data:
        writer.writerow(data) 

