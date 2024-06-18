import numpy as np

'''
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1

Make this array without manually typing.
'''
output = np.ones((5,5),dtype='int32')
#print(output)

zeros = np.zeros((3,3),dtype='int32')
#print(zeros)

#adding 9 in centre
zeros[1,1] = 9
#print(zeros)

#adding zeroes arr in output
output[1:4,1:4] = zeros #4 becuz it is excluded
print(output)