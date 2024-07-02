import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

labels = ['A','B','C']
values = [1,4,3]
bars = plt.bar(labels,values)
#we can do the properties of line chart here as well like resize, labels, titles, legends etc.

#setting hatch
'''
bars[0].set_hatch('O')
bars[1].set_hatch('\\')
bars[2].set_hatch('*')
'''
patterns = ['/','O','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.savefig('barchart.png')
plt.show()
