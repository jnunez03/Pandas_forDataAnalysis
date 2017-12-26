import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

### Dataset cars ^^ 


cars.head()

cars.sum() # A count for each of the values in each column. 

cars.sum(axis=1) # for each row, python generated a count horizontally.

        # median
        
cars.median() # median for each column!

cars.mean() # average

cars.max() # 33.9 max

# let's find where this comes from.
mpg = cars.mpg
mpg.idxmax()
# returns row where max was found: row 19. 

cars.car_names[19] # It was the Toyota Corolla!

cars.std() #std for each variable

cars.var()

# How many unique values present in data set.

gear = cars.gear
gear.value_counts() # 15 cars with 3 gears. 12 cars with 4 gears. 5 cars with 5 gears.

# Full stats of each variables

cars.describe()