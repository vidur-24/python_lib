import numpy as np

#load data from file
filedata = np.genfromtxt(r"C:\Users\duavi\Documents\code\python_libs\python_lib\numpy\data.txt", delimiter=',')
#for preventing file not found, in terminal cd to numpy
print(filedata) #float format
print(filedata.astype('int32')) #int format (its a copy)
#give file name or path (here file not found so given path)
#delimiter = seperator
print()


#boolean masking and advanced indexing
print(filedata > 50) #iterates over each element and replaces it with boolean value
print(~((filedata>50) & (filedata<100)))
print(filedata[filedata>50]) #prints the elemenst which are >50
print()


#
print(np.any(filedata>50, axis=0)) #returns boolean value for each column that contains any value >50
print(np.any(filedata>50, axis=1)) #returns boolean value for each row that contains any value >50
print(np.all(filedata>50, axis=0)) #returns boolean value for each column that contains all value >50
print(np.all(filedata>50, axis=1)) #returns boolean value for each row that contains all value >50
#axis=0 --> columns
#axis=1 --> rows
print()


#you can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]]) #prints elements at index 1 2 8 --> [2 3 9]
print()

