import numpy as np
# creating an input array.
myarray = np.array([[1,2,3],[4,5,6]])
# to flatten the array in F-order.
print(myarray.flatten('F'))