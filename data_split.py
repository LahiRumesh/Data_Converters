import pandas as pd

dataset=pd.read_csv("train_data_set.txt",delimiter="\n")
dataset_copy = dataset.copy()
train_set = dataset_copy.sample(frac=0.87, random_state=0)
test_set = dataset_copy.drop(train_set.index)

train_set.to_csv('train.txt', header=True, index=False, sep='\n', mode='a')
test_set.to_csv('val.txt', header=True, index=False, sep='\n', mode='a')