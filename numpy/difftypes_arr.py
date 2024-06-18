import numpy as np

#all 0s matrix
print(np.zeros((2,4,3))) #default dtype='float64'
print("\n")

#all 1s matrix 
print(np.ones((4,2), dtype='int32')) #can also specify data type
print()

#any other number
print(np.full((2,3),99,dtype='float32'))
print()

#any other number(full-like)
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.full_like(a,4)) #takes shape from diff array, here a
print()

#random decimal numbers bw 0 & 1
print(np.random.rand(4,2,3))
print()
print(np.random.random_sample(a.shape)) #for shape from diff arr
print("\n")

#random int values
print(np.random.randint(3,8, size=(3,3))) #from 2 to 8(excluded). if no start value then 0 by default
print()

#identity matrix
print(np.identity(3, dtype='int32')) #default dtype='float64'
print()

#repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0) #axis means which dimension to repeat i.e, 0 means outermost
print(r1)
r2 = np.repeat(arr,3,axis=1)
print(r2)
brr = np.array([1,2,3])
r3 = np.repeat(brr,4,axis=0)
print(r3)
print()
