# DO SAME AS pc2_ex_fifa.py BUT CHANGE WEUGHT DISTRIBUTION TO KGS.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Read
fifa = pd.read_csv('fifa_data.csv')
# print(fifa.head())

# Data
# print(fifa.Weight) --> it has lbs at end of each data
# removing lbs from each data so we get the value
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
# print(type(fifa.Weight[0]))

light = fifa.loc[fifa.Weight<125].count()[0]
light_medium = fifa.loc[(fifa.Weight>=125)&(fifa.Weight<150)].count()[0]
medium = fifa.loc[(fifa.Weight>=150)&(fifa.Weight<175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight>=175)&(fifa.Weight<200)].count()[0]
heavy = fifa.loc[fifa.Weight>=200].count()[0]

# Config
weights = [light,light_medium,medium,medium_heavy,heavy]
labels = ['<125','125-150','150-175','175-200','>200']
explode = (0.4,0.1,0,0.1,0.4) # respectively of above labels
#styles of pie chart (can search for more)
plt.style.use('ggplot') #changes color scheme, font, size etc.
plt.title('Weight Distribution of FIFA PLayers (in lbs)')
#NOTE: if we use title or any other style element that is affected by plt.style.use then this plt.style.use is not applied

# PIE CHART 2
plt.pie(weights, labels=labels, autopct='%.2f%%', pctdistance=0.9, explode=explode) 
# pctdistance = distance of % from centre of pc
# explode = to split the graph apart i.e, distance that part from centre

plt.show()