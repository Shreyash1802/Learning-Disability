# -*- coding: utf-8 -*-
"""Best_Fit_SVMGridSearch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vqeyvPopP4o3hzyk8uWe4Zzmd4XkK3St
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.metrics import classification_report
# %matplotlib inline

#In the Dyslexia notebook, it was found that SVM with GridSearch is the best fit for the given dataset.
#This model gives the most accurate predictions.
#In this notebook, we will create only a SVM with GridSearch model, which will then be used to make final predictions.

#Reading the dataset
data=pd.read_csv('Project_dataset.csv')
#Value to be predicted by the model.
y=data.Label
#Input taken by the model.
X=data.drop(['Label'],axis=1)
data.head()

#In the given data, the label is the indication for whether the person has dyslexia or not.
#Label = 1 means that there is a high chance that the person has dyslexia.
#Label = 2 means that there is a moderate chance that the person has dyslexia.
#Label = 3 means that there is a low chance that the person has dyslexia.

#Creating the test and train data sets for the given data.
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.8,random_state=10)

#StandardScalar is used for preprocessing of data.
#'copy' is False, which means copies are avoid and inplace scaling is done instead.
sc=StandardScaler(copy=False)
sc.fit_transform(X_train)
sc.transform(X_test)

#options_parameters is a list of dictionaries to find the most suitable values of 'kernel', 'gamma' and 'C' for the given model.
options_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]
#Creating SVM model with the most suitable parameters obtained by using GridSearch.
model = GridSearchCV(SVC(), options_parameters,scoring='f1_macro')
#Training the model.
model.fit(X_train, y_train)
#Making predictions using the model.
predictions = model.predict(X_test)
#Printing the values of 'C', 'gamma' and 'kernel' used in our model.
#These values provide the most accurate predictions for the given dataset.
print('Best parameters of SVM model are:')
print(model.best_params_)