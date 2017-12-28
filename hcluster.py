import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster, cophenet
from scipy.spatial.distance import pdist

import sklearn
from sklearn.cluster import AgglomerativeClustering

from pylab import rcParams

import sklearn.metrics as sm
from sklearn import datasets

np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10,5))
plt.style.use('seaborn-whitegrid')

# we will use mtcars.csv data set.

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
# we want mpg, disp, hp, wt. 1,3,4,6
X = cars.ix[:, (1,3,4,6)].values
y = cars.ix[:,(9)].values # am variables values.

# linkage on X, this carries our hierarchical clustering, ward linkage methods. output as Z.

Z = linkage(X,'ward')
dendrogram(Z,truncate_mode='lastp',p=12, leaf_rotation=45., leaf_font_size=15., show_contracted=True)
plt.title("Truncated Hierarchical Clustering Dendrogram")
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.axhline(y=500)
plt.axhline(y=150)
plt.show()

# we know based on our data that am variable takes on value 0 or 1. 
# based on that, pick 2 as number of clusters!

# if we use 2, we have a distance greater than 400. 

# k - number of clusters
k = 2
# CREATE MODEL
# affinity is distance metric - euclid.
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='ward')
# FIT MODEL
Hclustering.fit(X)

# accuracy ??
sm.accuracy_score(y, Hclustering.labels_) # .78 accuracy. 

                 # ---- Try Again, changing linkage ---- #
    
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='complete')
Hclustering.fit(X)
sm.accuracy_score(y, Hclustering.labels_) # .43 accuracy.

                 # ---- Again, change linkage ---- #
                 
Hclustering = AgglomerativeClustering(n_clusters=k, affinity='manhattan',linkage='average')
Hclustering.fit(X)
sm.accuracy_score(y, Hclustering.labels_)     # .78125  Highest.        
