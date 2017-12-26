import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize']= 7,6

""" Outliers

Point outliers: observations with respect to the majority of observations in a feature
aka univariate outlier.

Contextual outliers: observations considered anomalous given a specific context.

82 degrees in florida is different than 82 degrees in moscow russia given that the 
month is January.

Collective outliers: a collection of observations anomalous but appear close to one
another because they all have a similar anomalous value.
_______
Tukey methods.
using boxplots and scatterplot matrices,
Density based spatial clustering with DBSCAN and PCA.

"""

# Univariate Methods: Tukey Boxplots. 
# boxplot whiskers are set at 1.5(IQR). any points passed this are considered outliers.
# a = Q1 - 1.5(IQR)
# b = Q3 + 1.5(IQR)


address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch05/05_01/iris.data.csv"

df = pd.read_csv(filepath_or_buffer = address,header=None,sep=',')
df.columns = ['Sepal Length', 'Sepal Width','Petal Length', 'Petal Width','Species']

X = df.ix[:,0:4].values # first 4 columns, and access values
y = df.ix[:,4].values  # target, which is specie names

df[:5]

# outliers from tukey boxplots.

df.boxplot(return_type='dict')
plt.plot()

# there were supposed to show outliers in sepal width
# isolate values from dataframe
Sepal_Width = X[:,1] # 2nd column.

iris_outliers = (Sepal_Width > 4)
df[iris_outliers]
# AGAIN with less than 2.
Sepal_Width = X[:,1] # 2nd column.

iris_outliers = (Sepal_Width < 2.05)
df[iris_outliers]

# tukey outlier labeling. 

X_df = pd.DataFrame(X)
X_df.describe()

# use them to find potential outliers. 

# for column 1.

"""
 IQR = 3.3 - 2.8
 1.5(IQR) = .75
 
 2.8 - .75 = 2.05
 3.3 + .75 = 4.05








