import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy.random import randn
from pandas import Series, DataFrame
from matplotlib import rcParams
"""

Line chart: To show changes over time.

Bar Chart: To show changes in categorical data

Pie Chart: To show categorical data as proportions of the whole. 

-------------------------------------------------------------------------------------


Two Methods For Plot Building:
    
    Functional Method: build plots by calling the plotting function on a variable
    or set of variables.
    
    Object-oriented method: You build a plot by first generating a blank "figure"
    object, then populate the object with plots and plot elements.
    
"""
rcParams['figure.figsize']= 7, 6
        
sb.set_style('whitegrid')


x = range(1,10)
y =[1,2,3,4,0,4,3,2,1]

plt.plot(x,y)


address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"

cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars['mpg']

mpg.plot()

df = cars[['cyl','wt','mpg']]
df.plot()


plt.bar(x,y)


mpg.plot(kind='bar')

mpg.plot(kind='barh')

x = [1,2,3,4,0.5]
plt.pie(x)
plt.show()
# to save. plt.savefig('pie_chart.jpeg')