import numpy as np
import pandas as pd
%%time
train = pd.read_csv("data/train.csv", sep=',')
#train.set_index("PassengerId", inplace=True, drop=True)
train.head()
quali=[]
quanti=[]
for i in train.columns:
    if train[i].dtypes=='object':
        quali.append(i)
    else:
        quanti.append(i)
print("Qualitative:",len(quali))
print("Quantitative:",len(quanti))