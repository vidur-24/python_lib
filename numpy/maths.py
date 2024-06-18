import numpy as np

#BASICS
a = np.array([1,2,3,4])
b = np.array([1,1,1,1])
# arr + const. (can be any operator) adds const. to every element
print(a-2) # --> [-1 0 1 2]
print(a*2) # --> [2 4 6 8]
print(a+b) # --> [2 3 4 5]
print()

#take sin/cos
print(np.sin(a))
print()


#LINEAR ALGEBRA
a = np.ones((2,3), dtype='int32')
b = np.full((3,2),2)
print(a)
print(b)
print()

#matrix multiplication
print(np.matmul(a,b)) #does matrix multiplication
print(a@b) #same as above
'''
a*b --> ERROR cuz shape not same
'''
print()

#finding determinant
c = np.identity(3)
print(c)
print(np.linalg.det(c))
print()


#STATISTICS
stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print()

print(np.min(stats)) # --> 1
print(np.max(stats)) # --> 6

#axis(outer to inner level i.e, axis=0 means outermost level)
print(np.min(stats, axis=0)) # --> [1 2 3]
print(np.max(stats, axis=0)) # --> [4 5 6]
print(np.min(stats, axis=1)) # --> [1 4]
print(np.max(stats, axis=1)) # --> [3 6]


#VECTORS

#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v1,v2])) #keeps stacking the entries

#horizontal stacking 
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack((h1,h2))) #can use (h1,h2) or [h1,h2] it just need to be a sequence

