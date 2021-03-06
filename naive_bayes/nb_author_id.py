#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print("Training  time: {0:.3f} seconds".format(time()-t0))
to = time()
pred = clf.predict(features_test)
print("Predict  time: {0:.3f} seconds".format(time()-t0))
print("Prediction: {0}".format(pred))
from sklearn.metrics import accuracy_score
to = time()
accuracy = accuracy_score(labels_test, pred)
print("Accuracy  time: {0:.3f} seconds".format(time()-t0))
print("The accuracy is: {0}".format(accuracy))
to  = time()
accuracy = accuracy_score(pred, labels_test)
print("Accuracy  time: {0:.3f} seconds".format(time()-t0))

print("The accuracy is: {0}".format(accuracy))
#########################################################


