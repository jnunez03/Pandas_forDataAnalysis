import numpy as np 
import pandas as pd
from pandas import Series, DataFrame
"""
When selecting and retrieving data, we have to have a data object from 
which to select and retrieve.

Let's create it now: series_obj
"""
series_obj = Series(np.arange(8), index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8'])
# np.arange creates a series of 8 values from 0 to 7.
# We give our rows names by using the index function.
print(series_obj)

# When you use square brackets with index value inside, it tells python to select
# And retrieve all records of that index. 

series_obj['row 7'] # select and retrieve the row labeled 7. Returns 6. 

# Return rows with integer index values 0 and 7.
series_obj[[0,7]] 


# Create Random Data Frame, using random number generator from numpy.
# seed allows you to get the same random numbers
np.random.seed(25)
# create 36 random numbers, shape it in 6 by 6 matrix.
Df_obj = DataFrame(np.random.rand(36).reshape(6,6), index = ['row 1','row 2','row 3','row 4','row 5','row 6'],columns = ['column 1','column 2','column 3','column 4','column 5','column 6'])
print(Df_obj)

# Calling .ix[] special indexer, pass in a set of row and column indexes
# To select and retrieve only those specific rows and columns!

Df_obj.ix[['row 2','row 5'],['column 5', 'column 2']]

""" Data Slicing """

# Data Slicing allows you to select and retrieve all records from starting index,
# to ending label-index, and every record in-between.

series_obj['row 3':'row 7'] # returns row 3, row 7, and everything in between.

""" Comparing with Scalars """

Df_obj < .2   # uses true and false

""" Filtering with scalars """

series_obj[series_obj > 6] # all rows that have value > 6.

""" Setting Values with scalars """

series_obj['row 1', 'row 5', 'row 8'] = 8
# Sets values in each of those rows to 8.

series_obj # will show the updated rows. 

          



