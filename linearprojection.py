import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import rcParams

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter

rcParams['figure.figsize']= 7,6
sb.set_style('whitegrid')

""" Linear Projection method for multivariate data.

1. Make sure outliers should make up less than 5% of total observations -
Adjust model parameters accordingly.

IMPORTANT DBSCAN model parameters:
    EPS and min_samples.
    
    eps - maximum distance between two samples for them to be clustered
    in the same neighborhood (start at .1)
    
    min_samples - min # of samples in a neighborhood for a data point to qualify
    as a core point (start with small sample size)
    
Adjust to make sure that we have less than 5% of total dataset size, labeled
as outliers. 
"""

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch05/05_01/iris.data.csv"

df = pd.read_csv(filepath_or_buffer = address,header=None,sep=',')
df.columns = ['Sepal Length', 'Sepal Width','Petal Length', 'Petal Width','Species']

data = df.ix[:,0:4].values # first 4 columns, and access values
target = df.ix[:,4].values  # target, which is specie names


model = DBSCAN(eps=.8, min_samples=19).fit(data)

# rest of parameters are defualt. Check for outliers

outliers_df = pd.DataFrame(data)
# check if proportion is < 5 % of total data
print(Counter(model.labels_))
print(outliers_df[model.labels_ == -1 ])
# 150 total obs, 6 have label -1. which is 4% !
# Visualize cluster
fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
colers = model.labels_
ax.scatter(data[:,2],data[:,1], c=colers, s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBSCAN for Outlier Detection') # SOME WHITE BALLS CAN'T BE SEEN!!!!!

         