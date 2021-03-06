# -*- coding: utf-8 -*-
"""Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gj4FozuJq6Bl_ldfxDpINcA0Ethto12k
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.metrics import f1_score

data = pd.read_csv('DS_DATESET.csv')
data.head()

data["Label"] = data["Label"].replace({'eligible':1,'ineligible':0})

required_features = ['CGPA/ percentage','Which-year are you studying in?',"Rate your written communication skills [1-10]","Rate your verbal communication skills [1-10]",'Major/Area of Study']
X = data[required_features].copy()
 
X['Which-year are you studying in?'] = X['Which-year are you studying in?'].replace({'First-year':1, 'Second-year':2, 'Third-year':3, 'Fourth-year':4})
X['Major/Area of Study'] = X['Major/Area of Study'].replace({'Computer Engineering':1, 'Electrical Engineering':2, 'Electronics and Telecommunication':3})
y = data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)
yhat = LR.predict(X_test)
print('F1 Score For Linear Regression : ',f1_score(y_test,yhat))

from sklearn import svm
c = svm.SVC(kernel='rbf')
c.fit(X_train, y_train) 
yhat2 = c.predict(X_test)
print('F1 Score For SVM : ',f1_score(y_test,yhat2))

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
yhat3=dt.predict(X_test) 
print('F1 Score For Decision Tree : ',f1_score(y_test,yhat3))

from sklearn.neighbors import KNeighborsClassifier
k = 100
n = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat4 = n.predict(X_test)
print('F1 Score For KNN : ',f1_score(y_test,yhat4))

from sklearn.naive_bayes import GaussianNB
g = GaussianNB()
g.fit(X_train, y_train)
yhat5 = g.predict(X_test)
print('F1 Score For Gaussian Naive Bayes : ',f1_score(y_test,yhat5))

