import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# Combining different dataframes into 1.

DF_obj = DataFrame(np.arange(36).reshape(6,6))

DF_obj_2 = DataFrame(np.arange(15).reshape(5,3))

DF_obj
DF_obj_2

""" 
To concatenate, use the concat() method which joins data from separate sources
into 1 combined data table. 

If you want to join objects based on their row index values, just call the pd.concat()
method on the objects you wante joined, and then pass in the axis=1 argument.

This concatenates by adding dataframe columns (in other words, joining on row index values.)
"""

# pd.concat([left_object, right_object], axis = 1)
# this joins based on row indeces. 
# This makes the output table "" Wider "". 
# along Column, will make output table "" Longer "".

pd.concat([DF_obj, DF_obj_2], axis = 1)
pd.concat([DF_obj, DF_obj_2])

# Dropping Data to reformat

# object_name.drop([row indeces])

DF_obj.drop([0,2])

# axis = 1 argument drops columns.

DF_obj.drop([0,2], axis=1)



# Adding data

series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
series_obj

# .join() method to join 2 data sources into 1. It joins on row index values.
# output with be  "" Wider "". 
variable_added = DataFrame.join(DF_obj,series_obj)
variable_added

# We could use append, it adds rows to the bottom of the table.

added_datatable = variable_added.append(variable_added,ignore_index=False)
added_datatable
# ignore_index = False doesn't reindex our output data frame

added_datatable1 = variable_added.append(variable_added,ignore_index=True)
added_datatable1

# sort rows in dataframe. specify column index upon which the DataFrame should be sorted
DF_obj.sort_values(by=[5], ascending=[False])
