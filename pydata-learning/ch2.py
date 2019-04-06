from collections import defaultdict
from collections import Counter
from pandas import DataFrame, Series
# import pandas as pd
import numpy as np
import json
import urllib as url

path = 'https://raw.githubusercontent.com/wesm/pydata-book/1st-edition/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in url.urlopen(path)]
frame = DataFrame(records)
frame['tz'][0]
tz_count = frame['tz'].value_counts()
# fill up missing items with 'unknown'
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'unknown'

tz_counts = clean_tz.value_counts()
# draw an image
tz_counts[:10].plot(kind='barh', rot=0)
# accquire the string information contains 'agent' 
results = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]
# select the opearating system information of the source
os = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
# group by the operating system
by_tz_os = cframe.groupby(['tz', os])
agg_counts = by_tz_os.size().unstack().fillna(0)
# to sort the most frequent items and get the top 10 from end
idxs = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(idxs)[-10:]
count_subset.plot(kind='barh', stacked=True)

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)


# the examples using the magic command as follows: %time %timeit
strings = ['foo', 'foobar', 'xyz', 'Roman', 'quz', 'python'] * 100000
# %time method1 : Wall time: 171 ms
# %timeit method1 : 10 loops, best of 3: 135 ms per loop
method1 = [x for x in strings if x.startswith('foo')]
# %time method2 : Wall time: 105 ms
# %timeit method2 : 10 loops, best of 3: 66.2 ms per loop
method2 = [x for x in strings if x[:3] == 'foo']

arr = np.array(range(10))
np.save('C:\arr', arr)

def get_counts(sequences):
    counts = defaultdict(int)
    for x in sequences:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
            
    return counts
    
def top_counts(count_dict, n=10):
    
    '''
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    '''
    counts = Counter(count_dict)
    return counts.most_common(n)
    

class Message:
    
    def __init__(self, msg):
        self.msg = msg
        
    def __repr__(self):
        return 'Message: %s.' % self.msg

