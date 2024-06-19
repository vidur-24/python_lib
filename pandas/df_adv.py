import numpy as np
import pandas as pd

newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(1,335))
print(newdf)
#rows=334, columns=5
#np.arange method same as range funct

'''
print(newdf.head()) #prints only first 5 rows
print(newdf.tail()) #prints only last 5 rows 
print(newdf.describe())
'''
print(type(newdf),end="\n\n") # --> pandas.core.frame.DataFrame i.e, it is a df data struct

#dtypes
print(newdf.head())
print(newdf.dtypes,end="\n\n") #gives datatype of each column
'''
newdf[0][1] = "Vidur" #changes 1st element (for row we've given 1 cuz we changed the index)
print(newdf.head())
print(newdf.dtypes,end="\n\n") #changes 0th column dtype to be object as in bw float there is a str datatype
'''
newdf[0][1] = 20 #GIVES WARNING but changes
print(newdf.head())
print(newdf.dtypes,end="\n\n") #doesnt changes dtype to object, converts 20 to float

#printing index(rows) and columns
print(newdf.index,end="\n\n") #prints index and its dtype and length
print(newdf.columns,end="\n\n") #prints columns details

#creates numpy arr from df
print(newdf.to_numpy())

#transpose of df
print(newdf.T)

#sorting index
print(newdf.sort_index(axis=0, ascending=False)) #sorts rows(axis=0) in descending order
print(newdf.sort_index(axis=1, ascending=False)) #sorts rows(axis=1) in descending order

#copying (view)
newdf_copy = newdf #this newdf_copy will be view of newdf i.e, changes in newdf_copy will reflect in newdf
#view(database term) = data in same memory location it only points to the data
'''
#these 2 creates a copy not a view i.e, changes in newdf_copy will not reflect in newdf
newdf_copy = newdf.copy() 
newdf_copy = newdf[:]
'''

#WARNING
'''
newdf[0][1] = 20 #GIVES WARNING but changes
This SettingWithCopyWarning is returned becuz we not know where will a view will be returned and where a copy,
so sometimes changes may reflect and sometimes may not.
Also, sometimes pandas for internal memory management decides wether to return a copy or a view
Therefore we use loc function
'''

#changing column name
newdf.columns = list('ABCDE')
print(newdf.head())

#using loc funct
'''newdf['A'][2] = 50 #GIVES WARNING'''
newdf.loc[2,'A'] = 50 
newdf.loc[1,0] = 100 #if a column name is not there then it creates that column with that name and enters value at that row and for rest row value given as NaN
print(newdf.head())

#to remove column(drop)
newdf.drop(0,axis=1) #removes column(axis=1) named 0
#NOTE: above returns a view not changes newdf in place
print(newdf.head())
#changing in place 
newdf = newdf.drop(0,axis=1)
print(newdf.head())

#accessing parts
print(newdf.loc[[2,3],['C','D']]) #prints 2 3 index of C D column
print(newdf.loc[:,['C','D']]) #prints all indexes of C D column
print(newdf.loc[[2,3],:]) #prints 2 3 index of all columns

print(newdf.loc[newdf['A']<0.3]) #prints all the columns but only that rows whose Ath column value is <0.3
print(newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)]) #complex query

#iloc function : uses number to access i.e, pure index numbering (0 to number)
print(newdf.head(), end="\n\n")
print(newdf.iloc[0,2]) #prints 1st row Cth column value
print(newdf.iloc[1:4, [0,2]]) #prints rows 2 3 4 and column A C

#to remove row
print(newdf.drop(1)) #default axis=0, so drops row 1 and returns a view
#to drop multiple row
print(newdf.drop([1,3,4]))
#to change inplace assign newdf this view, just like in case of drop column (line 70)
#Another method to change in place
newdf.drop([1,3,4],axis=0,inplace=True) #inplace modifies inside memory location
print(newdf.head())

#to reset index (0 to number)
print(newdf.reset_index())
print(newdf.reset_index(drop=True)) #if drop=False then it creates a column named index and stores values as old index
newdf.reset_index(drop=True,inplace=True)
print(newdf.head())

#checks null values
print(newdf['C'].isnull()) #returns a series of bool values where the value in row is null i.e, 0

#makes every value of column B None
newdf['B'] = None #not preferred (same reason WARNING)
newdf.loc[:,['B']] = None #preffered
print(newdf)
print(newdf['B'].isnull())
print()

#drop rows with null
df = pd.DataFrame({
    "name" : ['Alfred','Batman','Alfred'],
    "toy" : [np.nan,'Batmobile','Bullwhip'], #NEW FUNCTIONS
    "born" : [pd.NaT,pd.Timestamp("1940-04-25"),pd.NaT] #NEW FUNCTIONS
})
print(df)
print(df.dropna()) #drops rows with any null values
print(df.dropna(how='all')) #drops rows with all null values
print(df.dropna(how='all',axis=1)) #drops column with all null values
#NOTE: they do not change original df


#drop duplicates
print(df.drop_duplicates()) #nothing happens (does not take axis as parameter)
print(df.drop_duplicates(subset=['name'])) #removes duplicates row which have repeated themselves in name column, but keeps the first duplicate
print(df.drop_duplicates(subset=['name'], keep='last')) #removes duplicates row which have repeated themselves in name column, but keep the last duplicate
print(df.drop_duplicates(subset=['name'], keep=False)) #removes all duplicates, doesnt keep any copy
print()

#get shape
print(df.shape, end="\n\n") # --> (3,3)

#give infor/details about df
print(df.info(),end="\n\n") 

#unique value count
print(df['name'].value_counts(dropna=False)) #give value count of each unique value in that column (includes None values as dropna=False)
print(df['toy'].value_counts(dropna=False)) #give value count of each unique value in that column (includes None values as dropna=False)
print(df['toy'].value_counts(dropna=True)) #give value count of each unique value in that column (doesnt includes None values as dropna=True)
print()

#checking null values
print(df.isnull()) #returns df with bool values which are null
print(df.notnull()) #returns df with bool values which are not null