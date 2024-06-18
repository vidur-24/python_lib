import numpy as np

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
#b[x,y,z]
'''[[[1 2]    
     [3 4]]

    [[5 6]
     [7 8]]]
'''
print("\n")

#get specific element (work out to in)
print(b[0,1,1]) #2nd element in 2nd element in 1st element in b --> 4
print(b[:,1,:]) 
'''[[3 4]
    [7 8]]
'''
print("\n")

#changing
b[:,1,:] = [[9,9],[8,8]]
print(b)
print("\n")

