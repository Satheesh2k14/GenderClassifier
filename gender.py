# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:25:31 2017

@author: Satheesh
"""

from sklearn import tree
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.svm import SVC
clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[190, 70, 43]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)


#Classifier 2
clf =  KNeighborsClassifier(3)

clf = clf.fit(X, Y)

prediction = clf.predict([[160,55,37]])

print(prediction)

#Classifier 3

#Classifier 2
clf =  SVC(kernel="linear", C=0.025)

clf = clf.fit(X, Y)

prediction = clf.predict([[175,75,37]])

print(prediction)