import random
from pandas import Series, DataFrame
import pandas as pd

position = 0
walk = [position]
step = 1000
for i in xrange(step):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
    
    
'''
Series
'''
sdata = {'Rihana':100000, 'Beyonce':120000, 'Jay-Z':240000, 'Mars':300000}
starts = ['Taylor', 'Beyonce', 'Jay-Z', 'Mars']
sdict = Series(sdata)
sdict2 = Series(sdata, index=starts)
sdict2
sdict + sdict2
 
   
'''
DataFrame
'''  
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
columns = ['year', 'state', 'pop']
# customize the order of the columns
frame = DataFrame(data, columns=columns)
# get a Series from DataFrame
series = frame['state'] 
indexes = ['one', 'two', 'three', 'four', 'five', 'six']
# customize the indexes
frame2 = DataFrame(data, columns=columns, index=indexes)   
# return a ndarray that presents the right columns of the data, and it is a view actually 
frame2.values
    