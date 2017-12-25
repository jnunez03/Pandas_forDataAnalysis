import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy.random import randn
from pandas import Series, DataFrame
from pylab import rcParams


rcParams['figure.figsize'] = 7, 6
sb.set_style('whitegrid')

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch02/02_05/Superstore-Sales.csv"

df = pd.read_csv(address, index_col = 'Order Date', parse_dates=True)
# //     Explanation: 
#   index_col this tells python to use order date column ad row labels for data frame.
#   parse_dates tells python parse index as set of dates.

df.head()


##  Order date is dataframe index. 

# Let's look at changes of order quantity over time.

df['Order Quantity'].plot() # too much data.

# let's take random sample of 100 samples. 

df2 = df.sample(n=100, random_state=25, axis=0) # axis=0 rows
# n=100 samples, random_state is seed, we want it to take rows. 

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('SuperStore Sales')

df2['Order Quantity'].plot()