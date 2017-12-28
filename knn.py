import numpy as np
import pandas as pd
import scipy
from pylab import rcParams
import matplotlib.pyplot as plt

import urllib
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
# just in case it was deprecated
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

np.set_printoptions(precision=4, suppress=True)
rcParams['figure.figsize'] = 7, 6
plt.style.use('seaborn-whitegrid')


# USE MTCARS.csv data set.

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

# We want to use AM as target.
# Our feature variables are mpg, disp, hp, and wt. 


X_prime = cars.ix[:,(1,3,4,6)].values
                  
y = cars.ix[:,9].values

           # scale variables
           
X = preprocessing.scale(X_prime)
# split 33% into test, 67% goes in training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)

# build model . KNN object

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)

# Evalute models prediction against test set.

y_expect = y_test  # just to give it more similar name
y_pred = clf.predict(X_test)
print(sm.classification_report(y_expect, y_pred))

# For points labeled 1, 67% of results returned were truly relevant.
# 82% for total data

# High precision - Low Recall means there were fewer results returned, but  many labels
# that are predicted returned correctly.

# IN other words, high accuracy, but low completion. 