import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# File Read
gas = pd.read_csv('gas_prices.csv')
# print(gas)

# Config
plt.figure(figsize=(8,5)) #if we save image with 300dpi, its resolution will be 2400x1500
plt.title("Gas Prices OverTime (in USD)", fontdict={'fontweight':'bold','fontsize':20})

# LINE GRAPHS
plt.plot(gas.Year,gas.USA, 'b.-') #year column of gas df as x axis and usa prices as y axis
# . is the another method to access column
# - means from one point to another it should be a straight line
plt.plot(gas['Year'],gas.Canada, 'r.-') #another country as y axis 
plt.plot(gas.Year,gas['South Korea'], 'g.-') #cannot use dot with columns having space
plt.plot(gas.Year,gas.Australia, 'y.-') 
'''
# easy way
countries_to_look_at = ['Australia','South Korea','USA','Canada']
for country in countries_to_look_at: #can also type "country in gas" for all countries 
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker='.', label=country)
'''

# Config
plt.xticks(gas.Year[::3].tolist() + [2011]) # places year skipping 3 so as to make it less cluttered
# to add 2011 year even if its not in df 
#NOTE: we need to convert df to list so that we can add 2011 year
# plt.xticks(gas.Year)
plt.xlabel('Year', fontdict={'fontweight':'bold','fontsize':12})
plt.ylabel('USD per gallon', fontdict={'fontweight':'bold','fontsize':12})
plt.legend(['USA','Canada','South Korea']) #can place legends in the order of plotting
#can also search for how to place legend outside plot

plt.show()

