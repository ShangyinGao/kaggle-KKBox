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
uniqueuser = set()
uniqueevent = set()
eventforuser = defaultdict(set)
userforevent = defaultdict(set)
for  i in all_df["msno"]:
    uniqueuser.add(i)
for i in all_df["song_id"]:
    uniqueevent.add(i)
for i in all_df.index:
    eventforuser[all_df.iloc[i,0]].add(all_df.iloc[i,1])
for i in all_df.index:
    userforevent[all_df.iloc[i,1]].add(all_df.iloc[i,0])
uniqueUserpair = set()
for event in uniqueevent:
    users = userforevent[event]
    if len(users) > 2:
        uniqueUserpair.update(itertools.combinations(users, 2))
file = open('uniqueUserpair.pickle','wb')
pickle.dump(uniqueUserpair,file)
file.close()