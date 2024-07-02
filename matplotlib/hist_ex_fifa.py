import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Read
fifa = pd.read_csv('fifa_data.csv')
# print(fifa.head())

# HISTOGRAM
bins = [0,10,20,30,40,50,60,70,80,90,100] #the range of x axis like 0-10,10-20 etc.
plt.hist(fifa.Overall,bins=bins, color='#abcdef') #using Overall column
#to see very low bar for ex 90-100 where players are very low use only 80,90,100 as bins
# for hex value of colors search 'color picker' on google

# Config
plt.xticks(bins)
plt.ylabel('No. of Players')
plt.xlabel('Skill Level')
plt.title("Distribution of Players Skills in FIFA 2018")

plt.show()
