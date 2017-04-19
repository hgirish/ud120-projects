#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
### These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data. 
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
import numpy as np
from sklearn.svm import SVC
#clf = SVC(kernel="linear")
for c in (10000.0,) :
    print("c is: {0}".format(c))
    clf = SVC(kernel="rbf", C=c)
    t0 = time()
    clf.fit(features_train, labels_train)
    print("Training  time: {0:.3f} seconds".format(time()-t0))
    to = time()
    pred = clf.predict(features_test)
    print("Predict  time: {0:.3f} seconds".format(time()-t0))
    print("Prediction: {0}".format(pred))
    unique, counts = np.unique(pred, return_counts=True)
    adict =dict(zip(unique,counts))
    print(adict[0])
    print(adict[1])
    sara = adict[0]
    chris = adict[1]
    print("Count for Sara  (0) is: ".format(sara))

    print("Count for Chris (1) is: ".format(chris))

    for i in (10,26,50):
        print("{0} prediction is {1}".format(i,pred[i]))
    from sklearn.metrics import accuracy_score
    
    to  = time()        
    accuracy = accuracy_score(pred, labels_test)
    print("Accuracy  time: {0:.3f} seconds".format(time()-t0))
    print("The accuracy is: {0}".format(accuracy))
#########################################################


