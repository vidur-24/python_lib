import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Read
fifa = pd.read_csv('fifa_data.csv')
# print(fifa.head())

# Data
# print(fifa['Preferred Foot'])
# print(fifa.loc[fifa['Preferred Foot'] == 'Left']) #this is a df
# print(left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()) #this is a series
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0] # this will return the count of 1st column of data frame i.e, no of left foot players
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0] # no of right foot players

# Config
labels = ['Left','Right']
colors = ['#abcdef','#ab3b22']
plt.title("Foot Preference of FIFA Players")

# PIE CHART 1
plt.pie([left,right], labels=labels, colors=colors, autopct='%.2f%%') #autopct for % of parts and %% for 1 sign

plt.show()
