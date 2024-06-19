import numpy as np
import pandas as pd

#DATAFRAME DATA STRUCTURE

#create df from dict
dict1 = {
    "name":['vidur','gauri','navya','seema','anshu'],
    "marks":[67,87,34,76,54],
    "city":['jalandhar','pune','banglore','jhansi','jhansi']
}
df = pd.DataFrame(dict1) #makes a dataframe just like excel sheet
print(df)
print()

#create csv from df
'''
df.to_csv('family.csv') #imports data to a csv file
df.to_csv('ifamily.csv', index=False) #imports but without index
'''

#accessing rows
print(df.head(2),end="\n\n") #prints first 2 rows of df
print(df.tail(2),end="\n\n") #prints last 2 rows of df
#in above 2 if no attribute given then prints first/last 5 rows
print(df.head(),end="\n\n")

#accessing statistics of df
print(df.describe(),end="\n\n") #prints statistical data of df

#read existing csv
train = pd.read_csv('train.csv') #reads data and created df from existing csv file
print(train, end="\n\n") #for preventing file not found, in terminal cd to pandas

#accessing column and its elements
print(train['Speed'],end="\n\n") #gives speed column of train df, also gives column name with datatype
print(train['Speed'][0], end="\n\n") #gives 0th row element of speed column --> 34

#to change value
'''
train['Speed'][0] = 50 #will GIVE WARNING but value changes
print(train)
train.to_csv('train.csv', index=False) #update the csv file
'''

#to change index
train.index = ['1st','2nd','3rd','4th','5th']
print(train)

