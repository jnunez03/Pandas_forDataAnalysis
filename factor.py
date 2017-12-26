import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy

import sklearn
from sklearn.decomposition import FactorAnalysis

# load iris dataset.
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data

variable_names = iris.feature_names

x[0:10,] # first 10 records, all columns

 
 # find latent variables, calling fit method.
 
factor = FactorAnalysis().fit(x)
 
# call dataframe on components attribute.
# columns = variable names. 

pd.DataFrame(factor.components_, columns=variable_names)

# components attribute represent factors with maximum variance.

