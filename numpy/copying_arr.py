import numpy as np

a = np.array([1,2,3])
b = a #shallow copy : changes in b is reflected in a
b[0] = 100
print(a)
print(b)
b = a.copy() #deep copy changes in b not reflected in a
b[0] = 100
print(a)
print(b)

a = np.array([[1,2],[3,4]])
b = a.copy()
b[0,1] = 100 #also works for 2d and 3d arr
print(a)
print(b)

'''
b = np.array(a) # also creates deep copy
'''