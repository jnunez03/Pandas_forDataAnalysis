import numpy as np 
from numpy.random import randn


# limit # of decimals returned.

np.set_printoptions(precision=2)

# create array 
a = np.array([1,2,3,4,5,6])

b= np.array([[10,20,30],[40,50,60]])

# create via assignment

np.random.seed(25)
c = 36*np.random.randn(6)

d = np.arange(1,35)


# arithmetic on arrays 

a * 10