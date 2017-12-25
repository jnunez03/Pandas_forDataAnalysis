import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy.random import randn
from pandas import Series, DataFrame
from pylab import rcParams


""" Plot Formatting Overview """

"""
1. Defining plot color
2. Customizing Line Styles
3. Setting marker styles
"""

# Parameters for our Visualization:
rcParams['figure.figsize'] = 7, 6
sb.set_style('whitegrid')

# Objects to plot

x = range(1,10)
y = [1,2,3,4,.5,4,3,2,1]

plt.bar(x,y)

# Adjust color, width, line width #

# width for each bar
wide = [.5, .5, .5, .9, .9, .9, .5, .5 ,.5] # Same as # of bars in chart

# color
color = ['salmon']
plt.bar(x,y,width=wide, color=color, align='center')

# Customize Colors for Pandas Object.

# ////////  We will use mtcars data set. \\\\\\\\\\\\\\\\ #

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


# Create Subset 
df = cars[['cyl', 'mpg', 'wt']]
df.plot()

# Colors

color_theme = ['darkgray', 'lightsalmon', 'powderblue']
df.plot(color = color_theme)

# pie chart

z = [1,2,3,4,.5]
plt.pie(z)
plt.show()

# Hex codes to customize colors.
colors = ['#A9A9A9','#FFA07A','#B0E0E6','#FFE4C4','#BDB76B']
plt.pie(z,colors=colors)
plt.show()



# Custom Line Styles

x1 = range(0,10)
y1 = [10,9,8,7,6,5,4,3,2,1]

plt.plot(x,y)
plt.plot(x1,y1)

# Restyle it
plt.plot(x,y,ls='steps',lw=5)
plt.plot(x1,y1,ls='--',lw=10)

# Change Marker Styles.

plt.plot(x,y, marker='1', mew=20)
plt.plot(x1,y1, marker='+', mew=15)
