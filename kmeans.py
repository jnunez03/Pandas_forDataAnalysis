import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report

plt.figure(figsize =(7,5))
# Load data set from sklearn

iris = datasets.load_iris()

# Scale data
# our x variable
X = scale(iris.data)

# our predictor variable - aka - target
y = pd.DataFrame(iris.target)

variable_names = iris.feature_names

# Print first ten records.
X[0:10,]

# Start cluster, instantiate a K-mean object - call it - clustering.
# n = 3 is centroids, we know there are 3 specie types of iris, so we put 3.
# random state is similar to setting a seed.
clustering = KMeans(n_clusters = 3, random_state=5)
# call fit method. 

clustering.fit(X)

# plot model outputs. 

iris_df = pd.DataFrame(iris.data)

iris_df.columns = ['Sepal_Length','Sepal_width','Petal_Length','Petal_Width']
y.columns = ['Targets']

# color for scatter
color_theme = np.array(['darkgray','lightsalmon','powderblue'])

# create subplot with 1 row 2 columns.
plt.subplot(1,2,1) # first plot
# Plot petal length against petal width.
# s  is marker size
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width,c=color_theme[iris.target], s=50) 
# Target variable is variable that contains species label!
# We want to color our data points BY their species label! 
# Lets give it a title
plt.title("Classification")

# ---- # -----# ----- # ----#
# We pass in value of 2, next scatterplot to be second of the 2 charts.
plt.subplot(1,2,2)
# We will color our data points according to their predicted species labels, not actual ones.
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width,c=color_theme[clustering.labels_], s=50) 
plt.title("KMeans classification")

# some are mislabeled. Numpys choose function.
# 0: should be changed to 2, 1: should be changed to 0, 2: should be one. 
relabel = np.choose(clustering.labels_, [2, 0, 1]).astype(np.int64)

# NOW COPY AND PASTE PLOT CODE .

plt.subplot(1,2,1) 
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width,c=color_theme[iris.target], s=50) 
plt.title("Classification")

# ---- # -----# ----- # ----#
# change clustering.labels_ to relabel
plt.subplot(1,2,2)
plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width,c=color_theme[relabel], s=50) 
plt.title("KMeans classification")



## Verify Quantitatively how accurate our models was, we use sklearn.
# y is target, relabel is our predicted variables that were relabelled. 
print(classification_report(y,relabel))

# Precision is a measure of the model's relevancy 
# Recall is a measure of the model's completeness

# We seek for high precision and high recall. 
# 83 % was correct.