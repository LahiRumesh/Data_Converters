import csv
from tqdm import tqdm
import argparse


def get_classes(classes_path):
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names


def main(DATA_CLASSES_FILE,INPUT_CSV_FILE,OUTPUT_CSV_FILE):
    classes=get_classes(DATA_CLASSES_FILE)
    input_file = csv.DictReader(open(INPUT_CSV_FILE))
    list_data=[]
    key=list(range(len(classes)))
    data_dict=dict(zip(key,classes))

    for row in tqdm(input_file):
        label=int(row["label"])
        for k, v in data_dict.items():
            if label==k:
                label=v

        list_data.append({
            "image" : row["image"],
            "xmin"  : row["xmin"],
            "ymin"  : row["ymin"],
            "xmax"  : row["xmax"],
            "ymax"  : row["ymax"],
            "label" : label
        })

    with open(OUTPUT_CSV_FILE,'w') as csvout:
        writer=csv.DictWriter(csvout,fieldnames=["image","xmin","ymin","xmax","ymax","label"])
        for data in list_data:
            writer.writerow(data) 

if __name__ == "__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--DATA_CLASSES_FILE", type=str, default="data_classes.txt", help="Input data classes file")
    parser.add_argument("--INPUT_CSV_FILE", type=str, default="detect.csv", help="Input CSV file name")
    parser.add_argument("--OUTPUT_CSV_FILE", type=str, default="out3.csv", help="Output CSV file name")
    args = parser.parse_args()
    main(args.DATA_CLASSES_FILE,args.INPUT_CSV_FILE,args.OUTPUT_CSV_FILE)
