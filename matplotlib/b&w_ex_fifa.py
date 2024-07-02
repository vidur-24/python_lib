import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Read
fifa = pd.read_csv('fifa_data.csv')
# print(fifa.head())

# Data
barcelona = fifa.loc[fifa.Club=='FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club=='Real Madrid']['Overall']
revs = fifa.loc[fifa.Club=='NE Revolution']['Overall']

# Config
plt.figure(figsize=(6,8))
labels = ['FC Barcelona','Real Madrid','New England Revolution']
plt.title('Soccer Team Comparision')
plt.ylabel('FIFA Overall Rating')

# BOX AND WHISKERS CHART
boxes = plt.boxplot([barcelona,madrid,revs], labels=labels, patch_artist=True, medianprops={'linewidth':2}) 
# patch artist for changing face color
# median props for changing median style

# Config
for box in boxes['boxes']: #'boxes' for boxes
    #we can also iterate a list in color for diff color of each box
    box.set(color='b', linewidth=2) #set edge color
    box.set(facecolor='#e0e0e0') #set fill color

plt.show()