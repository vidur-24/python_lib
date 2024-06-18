import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,1,1,1])
# arr + const. (can be any operator) adds const. to every element
print(a-2) # --> [-1 0 1 2]
print(a*2) # --> [2 4 6 8]
print(a+b) # --> [2 3 4 5]

#take sin/cos
print(np.sin(a))