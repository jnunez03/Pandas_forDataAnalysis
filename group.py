import pandas as pd
import numpy as np
from pandas import Series, DataFrame


""" 
You can group data in order to compare subsets and deduce reasons why subgroups differ
the way they do or you may only be interested in specific subgroups for analysis.

"""

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"

cars = pd.read_csv(address)


cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

cars.head() # returns first 5 records.

         
""" Lets group our data based on # of cylinders. """


cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()

# we grouped them by cylinders and then each subgroup, a mean
# has been taken. 

