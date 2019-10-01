#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Loading Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#importing dataset
data = pd.read_csv("E:\\Datasets\\DataSet\\Family Income.csv")

#checking null values
data.isnull().sum()
 
#dropping null values (or) replacing values with mean/most_frequent 
data = data.drop(['Household Head Occupation','Household Head Class of Worker'],axis=1)

#converting categorical into binary
from sklearn.preprocessing import LabelEncoder
lencoder = LabelEncoder()
data.iloc[:, 25:26]= lencoder.fit_transform(data.iloc[:,25:26])
data.iloc[:, 29:30]= lencoder.fit_transform(data.iloc[:,29:30])

#slicing the data
x= data.iloc[:,[2,14,15,18,20,24]]
y= data.iloc[:,0]
x.columns

#Model selection  and splitting
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#model implimentation
from sklearn.svm import SVR
regressor  = SVR(kernel = 'linear')
regressor.fit(x_train,y_train)

#model prediction
regressor.predict(x_test)

#model metrics
a=regressor.score(x_train,y_train)
b=regressor.score(x_test,y_yest)

#checking vif
vif = 1/(1-a)
print(a)
print(b)
print(vif)


# In[ ]:




