import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy.random import randn
from pandas import Series, DataFrame
from pylab import rcParams


# Parameters for our Visualization:
rcParams['figure.figsize'] = 7, 6
sb.set_style('whitegrid')

# objects for our plot.
x = range(1,10)
y = [1,2,3,4,.5,4,3,2,1]
plt.bar(x,y)

plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')


# label pie chart

z = [1, 2, 3, 4, .5]
veh_type = ['bicycle', 'motorbike', 'car', 'van', 'stroller']
plt.pie(z, labels=veh_type)
plt.show()

# object - Oriented Method

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars.mpg

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')

ax.set_title('Miles Per Gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('MPG')

# Legend!

plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()

# Object oriented method

fig = plt.figure()
ax= fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')

ax.set_title('Miles Per Gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('MPG')

ax.legend(loc='best')

#  --   --   --  --  ANNOTATIONS ! --  -  - - -- #


mpg.max()

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_title('Miles Per Gallon of cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('MPG')
ax.set_ylim([0,45])

ax.annotate('Toyota Corolla', xy=(19,33.9),xytext=(21,35),arrowprops=dict(facecolor ='black',shrink=.05))
# xy to mark location annotating! 
# 19 is record # of max value and 33.9 is max. 
# xytext = location where you want it to be placed