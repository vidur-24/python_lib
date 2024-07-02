import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#graph plot and line properties
x = [0,1,2,3,4]
y = [0,2,4,6,8]

#resize your graph
plt.figure(figsize=(5,3), dpi=100) #figsize is the ratio of x and y and dpi is pixels per inch or ratio

plt.plot(x,y, label='2x', color='blue', linewidth=2, linestyle='--', marker='.', markersize=10, markeredgecolor='black') #plots the graph
#color: can also give hexdec code for color
#linewidth: line ka motapa
#marker: points of x and y
#markersize: marker ka motapa
#markeredge color: colored edge of marker
#linestyle: how line appears
#NOTE: for these valid linestyle, color, marker, and other plot parameters, look in documentation
'''
#shorthand notation for plotting
#format = '[color][marker][linestyle]'
plt.plot(x,y, 'r^--', label='2x')
'''

#line 2
x2 = np.arange(0,4.5,0.5)
# plt.plot(x2,x2**2,'r', label='x^2')
plt.plot(x2[:6],x2[:6]**2,'r', label='x^2') #to make different parts of graph
plt.plot(x2[5:],x2[5:]**2,'r--', label='x^2')


#graph heading
plt.title("Our First Graph!", fontdict={'fontname':'Comic Sans MS', 'fontsize':20})

#graph axis labels
plt.xlabel("X Axis") #can also use fontdict for x and y label
plt.ylabel("Y Axis")

'''
#graph x and y axis marked points
plt.xticks([0,1,2,3,4]) 
plt.yticks([0,2,4,7,3,6,8,10])
#it resizes graph based on these ticks
'''

#put legend: label for line
plt.legend()

#save graph (dpi 300 is good when saving so graph has high resolution)
plt.savefig('linegraph.png', dpi=300) #will save in the curr dir


plt.show() #prints the graph
