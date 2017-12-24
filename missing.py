import pandas as pd
import numpy as np
from pandas import Series, DataFrame

""" MISSING VALUES: 
    
    1. How de we discover whats missing from our data
    
    2. Filling in for missing values
    
    3. Counting Missing Values
    
    4. Filtering out missing values 
    
"""

# Let's create a series object that contains missing values.

missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4', 'row 5', 'row 6', missing, 'row 8'])
series_obj
# isnull() returns a boolean value that describes whether an element in pandas object is a null value. 
series_obj.isnull()

# use a random data frame

np.random.seed(25)

DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj

# that was our randomly generated data frame object. We want to set some to NaN.
# lets set record 3 thru 5 in column index 0 to Nan, 1 thru 4 in column index 5 to Nan.

DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
DF_obj

# object_name.fillna(numeric Value) 

filled_DF = DF_obj.fillna(0)

# you could pass in dictionary..
# FOR VALUES IN COLUMN 1, fill with .1 , FOR COLUMN 5 values fill them in with 1.25
filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})

# ffill. Fill Forward Method. 

# ffil: missing values in a column are filled with the last non-null value encountered from withing
# that same column

fill_DF = DF_obj.fillna(method='ffill')
fill_DF

""" Count Missing Values """

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
DF_obj



DF_obj.isnull().sum() # Returns a count for EACH column.

# filtering out. dropna

DF_no_NaN = DF_obj.dropna() # DROPS ALL ROWS THAT HAVE MISSING VALUES

# drop columns we use axis = 1. 
DF_no_NaN = DF_obj.dropna(axis=1)

DF_obj.dropna(how='all') # drops rows that only have NAn's. 

