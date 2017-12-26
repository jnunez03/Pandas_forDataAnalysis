import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

""" Categorical Variables 

Basic ways to describe them:
    summarized by counts, grouping, variable descriptions, or cross-tabulations.
    
    
    A crosstab is a cross tabulation of 2 or more features.
    It shows frequency counts for features. EX: 2 variables: gear and am.
    
    
                     gear  3   4   5
                 am |________________
                 0  |     15   4   0
                 1  |     0    8   5
"""

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head(15)

carb = cars.carb
carb.value_counts() # quantify data set to not miss anything by using head()

# Create small subset of categorical variables.

cars_cat = cars[['cyl','vs','am','gear','carb']]
cars_cat.head()

# how to group by gears variable.
gears_group = cars_cat.groupby('gear')
gears_group.describe()

# How to create categorical variable..
cars['group'] = pd.Series(cars.gear, dtype="category")
# Here we create a new categorical series from the gear variable, and new column in the cars DataFrame and called it group.
cars['group'].dtypes # type of variable
    
cars['group'].value_counts()

# Cross tabs ...

pd.crosstab(cars['am'],cars['gear'])