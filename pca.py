import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy

from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets


rcParams['figure.figsize']= 7, 6
sb.set_style('whitegrid')

iris = datasets.load_iris()
x = iris.data
variable_names = iris.feature_names

x[0:10,]

pca = decomposition.PCA() # pca object.

iris_pca = pca.fit_transform(x)

pca.explained_variance_ratio_
pca.explained_variance_ratio_.sum() # we get 1 cumulative variance. 100% of data information
# is captured from 4 components.

# explained variance ratio tells us how much information is compressed into the first
# few components.

# When deciding how many components to keep, look at % of cumulative variance. 
# Make sure to retain at least 70% of the dataset's original information.

# However, we don't 100% of the information. some of it has noise, info redundancy. We only
# want to keep the principle components that matter.

# First value was .9246, and 2nd was .05301. 
# This contains 97.7  % of iris datasets original information.

comps = pd.DataFrame(pca.components_,columns=variable_names)

sb.heatmap(comps)

# 0 is 1st comp, 1 is 2nd comp, the components we decided to keep.
# principal component 1 is strongly positively correlated with petal length
# Also moderately positively correlated with petal width and sepal length.

# you can use them as input variables for ml algorithms. 



