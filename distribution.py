import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

# using mtcars.csv file in files section

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch01/01_05/mtcars.csv"
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

rcParams['figure.figsize'] = 7,6
plt.style.use('seaborn-whitegrid')


mpg = cars.mpg

plt.plot(mpg)

cars[['mpg']].describe()

# transformation. place in 1 column matrix.

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg)

plt.plot(scaled_mpg)


# scale to different range... use feature range arguments.

mpg_matrix = mpg.reshape(-1,1)
scaled = preprocessing.MinMaxScaler(feature_range=(0,10))
scaled_mpg = scaled.fit_transform(mpg)

plt.plot(scaled_mpg)


# Standardized.

standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)

plt.plot(standardized_mpg)
# plot is original, no changes.. 

std_mpg = scale(mpg)
plt.plot(std_mpg)
# it becomes standardized. 

