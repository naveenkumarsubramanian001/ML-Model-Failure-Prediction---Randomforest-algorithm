# -*- coding: utf-8 -*-
"""ML Model Failure Prediction - Randomforest algorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SOhtEsuid7TrDp6N60xTOb3Os9V4cMJx
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

class_data= pd.read_csv('/content/data.csv')

class_data.head()

class_data.shape

class_data.isnull().sum()

model = RandomForestClassifier( n_estimators=100, max_depth=5, random_state=42)

X = class_data.drop(['fail'], axis=1)
Y = class_data['fail']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state =42 )

model.fit(X_train, Y_train)

model.predict(X_train)

train_pred = model.predict(X_train)
accuracy_score(Y_train, train_pred)

test_pred = model.predict(X_test)
accuracy_score(Y_test, test_pred)

input = (190,1,3,3,5,1,20,4,1)
input = np.asarray(input)
input = input.reshape(1, -1)
pred = model.predict(input)
print(pred)
if (pred== 0):
  print('Model Failed')
else:
  print('Model is Successfull')

report = classification_report(Y_test, test_pred)
print(report)

con_mat = confusion_matrix(Y_test, test_pred)
print(con_mat)

