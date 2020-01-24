import csv
from tqdm import tqdm


INFILE="input.csv"
OUTFILE="output.csv"
Label_OUT="label.csv"

csv_file=open(INFILE)

data_file=csv.DictReader(csv_file,fieldnames=["image","location","xmin","ymin","xmax","ymax","label"])

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

    list_label.append({
       "label" : row["label"]
       
       })

with open(OUTFILE,'w') as csvout:
    writer=csv.DictWriter(csvout,fieldnames=["image","xmin","ymin","xmax","ymax","label"])
    for data in list_data:
        writer.writerow(data) 

csv_file.close()

with open(Label_OUT,'w') as csvout:
    writer=csv.DictWriter(csvout,fieldnames=["label"])
    for data in list_label:
        writer.writerow(data)
 
csv_file.close()

