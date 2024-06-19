import numpy as np
import pandas as pd
#need to install xlrd and openpyxl module 

#to read excel sheets
data1 = pd.read_excel('data.xlsx') #reads Sheet1
print(data1,end="\n\n")
data2 = pd.read_excel('data.xlsx',sheet_name='Sheet2') #reads Sheet2
print(data2,end="\n\n")

data1.iloc[0,0] = 100
print(data1)

#import data in excel
'''data1.to_excel('data.xlsx', sheet_name='Sheet1') #writes data of data1 df to Sheet1 of excel sheet'''
#NOTE: this will remove the Sheet2 of data sheet
#to write more than one sheet refer to resources.md

