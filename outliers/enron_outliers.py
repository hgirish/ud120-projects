#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
removed = data_dict.pop('TOTAL',0)
#print(removed)

for k, v in data_dict.iteritems():
 if type(v) is dict:
     if float(v['salary']) >= 1000000 and float(v['bonus']) >= 5000000. :
         print(k,v['salary'], v['bonus'])

  #for t, c in v.iteritems() 
 #  if t == 'bonus' and float(c) >= 5000000. and c != 'NaN':
#     print(t, c, k)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

