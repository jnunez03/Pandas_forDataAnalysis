import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import scipy
from scipy.stats.stats import pearsonr

""" Parametric correlation analysis


Correlation does not imply causation


How to calculate pearson correlation method. 

Assume:
    
1. data is normally distributed.
2. have continuous, numeric variables
3. Variables are linearly related
"""

rcParams['figure.figsize']= 7, 6
plt.style.use('seaborn-whitegrid')

#   USE mtcars.csv file uploaded in files

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

sb.pairplot(cars) # scatter plot matrix.
# we see barplot at bottom right, which is not continuous numeric, but binomial or multinomial

x = cars[['mpg', 'hp', 'qsec', 'wt']]

sb.pairplot(x)

# Check our assumptions.
# normal should give us bell curve shape.


mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg,hp)
print(pearsonr_coefficient, p_value)

pearsonr_coefficient, p_value = pearsonr(mpg,qsec)
print(pearsonr_coefficient, p_value)

pearsonr_coefficient, p_value = pearsonr(mpg,wt)
print(pearsonr_coefficient, p_value)

# Same but done for each variable in our x variables.
corr = x.corr()
print(corr)
sb.heatmap(corr, xticklabels = corr.columns.values, yticklabels = corr.columns.values)

# this shows hp and wt have highest degree of positive relation
# qsec and wt have no linearity, but it doesn't mean there is no correlation.

