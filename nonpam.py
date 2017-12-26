import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import scipy
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency



""" Non-Parametric correlation analysis 

Spearman's rank - chi-square tables to establish correlation
between categorical variables.

Assumptions:
    1. variables are ordinal
    2. variables are non-linear
    3. data is non-normally distributed

Chi-sqaured tables to test for independence.
p < .05 variables are correlated
p > .05 variables aren't correlated


#  When to use chi-sqaured tables?
1 - your variables are categorical or numeric.
2 - you have binned the numeric variables. 
How many are from 0-10, 11-20, 21-30, 31-40, 41-50, 51-60, 61- 70, etc.

"""

rcParams['figure.figsize'] = 14, 7
plt.style.use('seaborn-whitegrid')

# data from mtcars.csv
address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

sb.pairplot(cars)

# subset of data 

x = cars[['cyl','vs','am','gear']]
sb.pairplot(x)
# check assumptions. Nonlinear, and not normal.

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print(spearmanr_coefficient) # -.814

spearmanr_coefficient, p_value = spearmanr(cyl, am)     
print(spearmanr_coefficient) # -.522

spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print(spearmanr_coefficient) # -.564

# Chi-sqaured test for independence.

table = pd.crosstab(cyl,am)

chi2, p, dof, expected = chi2_contingency(table.values)
print(chi2, p) # chi- 8.741, p = .013

table1 = pd.crosstab(cyl,vs)
chi2, p, dof, expected = chi2_contingency(table1.values)
print(chi2, p) # chi- 21, p = 2.2e-5

table2 = pd.crosstab(cyl,gear)
chi2, p, dof, expected = chi2_contingency(table2.values)
print(chi2, p) # chi- 18, p = .001

     
# none of the pvalues are greater than .05 and prove variables are 
# correlated. 

