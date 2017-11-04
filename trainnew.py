import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import itertools
import pickle
from collections import defaultdict
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
members = pd.read_csv("members.csv")
train_u_e = train.iloc[:,:2]
test_u_e = test.iloc[:,1:3]
all_df = pd.concat((train_u_e,test_u_e), axis = 0, ignore_index= True)
class_le = LabelEncoder()
y1 =class_le.fit_transform(all_df["msno"].values)
y2 = class_le.fit_transform(all_df["song_id"].values)
uniqueuser = set()
uniqueevent = set()
eventforuser = defaultdict(set)
userforevent = defaultdict(set)

uniqueuser = set()
uniqueevent = set()
eventforuser = defaultdict(set)
userforevent = defaultdict(set)
for i in y1:
    uniqueuser.add(i)
for i in y2:
    uniqueevent.add(i)
for i in all_df.index:
    eventforuser[y1[i]].add(y2[i])
for i in all_df.index:
    userforevent[y1[i]].add(y2[i])
uniqueUserpair = set()
print("finish")
for event in uniqueevent:
    users = userforevent[event]
    print('finish')
    if len(users) > 2:
        uniqueUserpair.update(itertools.combinations(users, 2))
file = open('uniqueUserpair.pickle','wb')
pickle.dump(uniqueUserpair,file)
file.close()