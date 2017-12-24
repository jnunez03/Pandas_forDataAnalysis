import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# Create our data frame.

DF_obj = DataFrame({'column 1': [1,1,2,2,3,3,3],
                    'column 2': ['a','a','b','b','c','c','c'],
                    'column 3': ['A','A','B','B','C','C','C']})

# We want to remove rows.
# object_name.duplicated()
# .duplicated() method searches each row, and returns True or False
# to indicate whether it is a duplicate of another row found earlier in DataFrame

DF_obj.duplicated()

# Drop the duplicates. Any rows that are duplicates of rows that came before.

DF_obj.drop_duplicates()


DF_obj = DataFrame({'column 1': [1,1,2,2,3,3,3],
                    'column 2': ['a','a','b','b','c','c','c'],
                    'column 3': ['A','A','B','B','C','D','C']})

DF_obj.drop_duplicates(['column 3'])

# Check for duplicates in column 3 and if found, drop the row! 
