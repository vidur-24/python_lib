import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
print()

#get specific element --> arr[r,c] , uses list index notations i.e, begins from 0
print(a[1,3]) #2nd row 4th elements --> 11
print()

#get specific row
print(a[0,:]) #prints 1st row (: is as per slicing rules)
print()

#get specific column
print(a[:,2]) #prints 3rd column
print()

#fancy: get elements bw 2 and 6 and by step size 2
print(a[0,1:6:2]) # --> [2 4 6]
print(a[0,6:1:-1]) # --> [7 6 5 4 3]
print()

#changing element
a[1,6] = 20
a[:,1] = 5 #changing whole column to be same element
a[:,1] = [1,2] #changing column to be diff element
print(a)

