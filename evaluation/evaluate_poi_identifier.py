#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Split into a training and testing set
feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size=0.30, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(feature_train, label_train)

pred = clf.predict(feature_test)
accuracy = accuracy_score(label_test, pred)
print("The accuracy is: {0}".format(accuracy))
