import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter

rcParams['figure.figsize']= 7, 6
sb.set_style('whitegrid')

# read in our data. Using enrollement.forecast.csv


address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch08/08_01/enrollment_forecast.csv"
enroll = pd.read_csv(address)

# name columns

enroll.columns = ['year','roll','unem','hgrad','inc']
enroll.head()

# We need to check out assumptions. 
# using scatterplot matrix.

sb.pairplot(enroll) # some are strong, and they are all continous numeric.

# check correlation. We don't want correlation between our predictor variables here.
print(enroll.corr())
# hgrad and unem pair show no correlation.
# hgrad and unem -2,3
enroll_data = enroll.ix[:,(2,3)].values
enroll_target = enroll.ix[:,1].values  # column retrieval.

enroll_data_names = ['unem','hgrad'] # column names for new dataframe.

# we need to scale our variables. 
X, y = scale(enroll_data), enroll_target

# check for missing values.
# bool returns
missing_values = X==np.NAN
X[missing_values == True] # returns rows with missing values

LinReg = LinearRegression(normalize=True)

LinReg.fit(X,y)

print(LinReg.score(X,y)) # 84.89 prediction accuracy. 