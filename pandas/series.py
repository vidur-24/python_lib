import numpy as np
import pandas as pd

#series data structure
ser = pd.Series(np.random.rand(34))
print(ser) #prints series of 34 random number bw 0 and 1 along with the series data type in end
print(type(ser)) # --> pandas.core.series.Series i.e, it is a series data struct

