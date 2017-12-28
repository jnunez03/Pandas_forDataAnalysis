import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import urllib
import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score

# from UC IRVINE data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"

raw_data = urllib.urlopen(url)

dataset = np.loadtxt(raw_data, delimiter=",")

print(dataset[0]) # huge matrix.

X = dataset[:,0:48]

y = dataset[:,-1]

# test/training set

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.33, random_state=17)

# Try bernoulli method, change frequencies to binaries

BernNB = BernoulliNB(binarize=True)
# FIT
BernNB.fit(X_train,y_train)

y_expect = y_test

y_pred = BernNB.predict(X_test)

print(accuracy_score(y_expect, y_pred))
# .855 prediction score.


# ---- Multinomial Naive Bayes ---- # 
MultiNB = MultinomialNB()
MultiNB.fit(X_train, y_train)

y_pred = MultiNB.predict(X_test)
accuracy_score(y_expect, y_pred)
# .877 accuracy score.

#--- Guassian ---#

GausNB = GaussianNB()
GausNB.fit(X_train, y_train)
y_pred = GausNB.predict(X_test)
accuracy_score(y_expect, y_pred)
# 81% accurate

## ----- Binarize value to 0.1
BernNB = BernoulliNB(binarize=0.1)
# FIT
BernNB.fit(X_train,y_train)

y_expect = y_test

y_pred = BernNB.predict(X_test)

print(accuracy_score(y_expect, y_pred)) # 89.5 % accuracy. 
