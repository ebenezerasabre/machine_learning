import pandas as pd
import numpy as np


d = {'col1': [1,2,3,4,7], 'col2':[4,5,6,9,5], 'col3':[7,8,12,1,11]}
df = pd.DataFrame(data=d)

count_column = df.shape[1]
count_row = df.shape[0]

Average_pulse_max = [80, 85, 90, 100, 105, 110, 115, 120, 125]
average = np.mean(Average_pulse_max)

data_csv = pd.read_csv("data_1.csv", header=0, sep=",")
#data_csv.dropna(axis=0,inplace=True)


#print(data_csv)
print(data_csv.info())
print(data_csv.describe())


