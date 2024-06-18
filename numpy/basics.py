import numpy as np

#basics
a = np.array([1,2,3], dtype='int16') #dtype to specify data type on own
print(a)
b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)
#cannot make a array as [[1.0,[2.0,3.0]],[4.0,5.0,6.0],[7.0,8.0,9.0]])
#cuz it will be a heterogeneous list and array is homogeneous
#also each should contain equal elements
print()

#get dimensions
print(a.ndim) # --> 1
print(b.ndim) # --> 2
print()

#get shape
print(a.shape) # --> (3,) as one dim therefore 3 size
print(b.shape) # --> (2,3) as 2 rows and 3 columns
print()

#get type
print(a.dtype) # --> int32
print(b.dtype) # --> float64
print()

#get size
print(a.itemsize) # --> 2
print(b.itemsize) # --> 8
print()

#get total size (2 ways)
print(a.size * a.itemsize) # --> 3*2 = 6
print(b.size * b.itemsize) # --> 6*8 = 48
print(a.nbytes) # --> 6
print(b.nbytes) # --> 48 
print()

#automatic type conversions
list = [6.1,4.6,3.4,9.0,8,1.6] #8 is int
res = np.array(list)
print(res) #8 converted to 'float64'
print(type(res))
print(type(res[0]))
print(res + 2)
print(res + 3.2)
#similarly if one type is str and other are int , then numpy arr implicitly converts int elements to str

#reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((4,2)) #will work as long as both shape has equal number of items
print(after)
