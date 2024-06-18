import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(a, end="\n\n")
'''
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20 
21 22 23 24 25 
26 27 28 29 30
'''

#Q1. we need to access 
'''
11 12
16 17
'''
print(a[2:4,0:2])

#Q2. we need to access
'''
2
    8
        14
            20 
'''
print(a[[0,1,2,3],[1,2,3,4]]) #1st list for row and 2nd list for column

#Q3. we need to access 
'''
4  5



24 25 
29 30
'''
print(a[[0,4,5],3:5])