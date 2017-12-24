import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from numpy.random import randn
from pandas import Series, DataFrame
from matplotlib import rcParams


""" Object oriented plotting:
    
    1. Create blank figure object
    
    2. Add Axes to figure
    
    3. Generate Plots within figure object
    
    4. Specify Plotting and layout parameters for the plots within the figure
    
    # How to generate subplots. 
"""

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) # left side, bottom, width, height
ax.plot(x,y)
# --------- # ------ #
# need to re-enter our fig and ax for each plot
fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) # left side, bottom, width, height
ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,4,5,6,8,9,10]) # 3 and 7 will not show in plot
ax.set_yticks([0,1,2,3,4,5])
ax.plot(x,y)

# -----# ------# ------# -----# -----# -----#

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1]) # left side, bottom, width, height
ax.set_xlim([1,9])
ax.set_ylim([0,5])
ax.grid()
ax.plot(x,y)

# -----# ------# ------# -----# -----# -----#
# -----# ------# ------# -----# -----# -----#

#     SUBPLOTS       # 

fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2) # row, column

ax1.plot(x)
ax2.plot(x,y)
