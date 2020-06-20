import csv
from tqdm import tqdm
import argparse



def main(DATA_CLASSES_FILE,INPUT_CSV_FILE,OUTPUT_CSV_FILE):
    input_file = csv.DictReader(open(INPUT_CSV_FILE))
    list_data=[]

    for row in tqdm(input_file):

        list_data.append({
            "image" : row["image"],
            "xmin"  : row["xmin"],
            "ymin"  : row["ymin"],
            "xmax"  : row["xmax"],
            "ymax"  : row["ymax"],
            "label" : row["label"]
        })

    with open(OUTPUT_CSV_FILE,'w') as csvout:
        writer=csv.DictWriter(csvout,fieldnames=["image","xmin","ymin","xmax","ymax","label"])
        for data in list_data:
            writer.writerow(data) 

if __name__ == "__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--DATA_CLASSES_FILE", type=str, default="10_data_classes.txt", help="Input data classes file")
    parser.add_argument("--INPUT_CSV_FILE", type=str, default="input/jan28.csv", help="Input CSV file name")
    parser.add_argument("--OUTPUT_CSV_FILE", type=str, default="output/281_tout.csv", help="Output CSV file name")
    args = parser.parse_args()
    main(args.DATA_CLASSES_FILE,args.INPUT_CSV_FILE,args.OUTPUT_CSV_FILE)
