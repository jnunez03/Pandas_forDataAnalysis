import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import seaborn as sb

from pandas.tools.plotting import scatter_matrix

from numpy.random import randn
from pylab import rcParams

""" Histograms, box plots, scatter plots """

rcParams['figure.figsize']= 7, 6
sb.set_style('whitegrid')

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.index = cars.car_names

mpg = cars['mpg']
mpg.plot(kind='hist')
# - or -
plt.hist(mpg)
plt.plot()
# - or -
sb.distplot(mpg)


## Seeing Scatterplots in action

cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
# In Seaborn

sb.regplot(x='hp', y='mpg', data=cars,scatter=True) # creates trendline.

# Scatter plot matrix

sb.pairplot(cars)

# Add a third dimension, by adding categorical coloring.
# we want to access the values (.values)
cars_df = pd.DataFrame((cars.ix[:,(1,3,4,6)].values), columns = ['mpg', 'disp', 'hp', 'wt'])
cars_target = cars.ix[:,9].values #column AM, column that is 9, and access values
target_names = [0, 1]   # a 0 for automatic, or 1 for manual.

# create new variable in cars dataframe.
# categorical variable. tell seaborn to go thru that variable, and color
# each point in matrix accoridng to value in that category..

cars_df['group'] = pd.Series(cars_target, dtype="category")
sb.pairplot(cars_df, hue='group', palette='hls')
# cars_df dataframe plotted, hue - pick colors for points based on values in group column
# palette hls is pre-built for colors. 

# red indicates automatic, blue indicates manual. 

# in wt graph
# its showing that cars that weight more tend to have automatic transmission.


# BOX PLOT !!! 


cars.boxplot(column='mpg', by='am')
cars.boxplot(column='wt', by='am')
# This tells us what we just saw in seaborn!

# EQUIVALENT CODE BELOW 

sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
                     
                     