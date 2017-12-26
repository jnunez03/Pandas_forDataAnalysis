import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize']= 7,6
sb.set_style('whitegrid')

address = "/Users/justinnunez/Downloads/Ex_Files_Python_Data_Science_EssT/Python4DSExecFiles/ch05/05_01/iris.data.csv"

df = pd.read_csv(filepath_or_buffer = address,header=None,sep=',')
df.columns = ['Sepal Length', 'Sepal Width','Petal Length', 'Petal Width','Species']

X = df.ix[:,0:4].values # first 4 columns, and access values
y = df.ix[:,4].values  # target, which is specie names


        
sb.boxplot(x='Species',y='Sepal Length', data=df,palette='hls')
# plotting 2 variables in 1 box plot. 

# using scatterplot matrices.

sb.pairplot(df,hue='Species', palette='hls') # hue is to color according to species.
# seems to be an outlier at sepal width ~ 2.3, Petal Width ~ .25 (red)


