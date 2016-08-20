# Part 1:

# Q1 ------------------
import pandas as pd
import numpy as np
df = pd.read_csv('faculty.csv')
cols = map(lambda c: c.strip(), df.columns.tolist())
df.columns = cols

df.degree = df.degree.apply(lambda d: d.strip().replace('.',''))
degs = set(df.degree.apply(lambda d: d.split(' ')).sum())
degs.discard('0')
# number of unique degrees in data:
len(degs)# 8

dummy_matrix = pd.DataFrame(np.zeros((len(df),len(degs))), columns = degs)
df = pd.concat([df, dummy_matrix], axis = 1)
for i in range(len(df)):
  if df.ix[i].degree == '0':
    continue
  df.ix[i, df.ix[i, 'degree'].split(' ')] = 1

df.ix[:,-8:].sum()

'''
MD       1.0
MA       1.0
ScD      6.0
BSEd     1.0
PhD     31.0
MPH      2.0
MS       2.0
JD       1.0
'''


# Q2 ------------------

# clearly a typo
df.loc[df.title == 'Assistant Professor is Biostatistics', 'title'] = 'Assistant Professor of Biostatistics'
df.title.unique()
# ['Associate Professor of Biostatistics', 'Professor of Biostatistics', 'Assistant Professor of Biostatistics']
df.title.value_counts()
'''
Professor of Biostatistics              13
Associate Professor of Biostatistics    12
Assistant Professor of Biostatistics    12
Name: title, dtype: int64
'''


# Q3  ------------------

# ...
df.email 
# i'm slightly confused by this section as it seems to be asking me about regex, 
# but even if i weren't using pandas i'd use csv and still just refer to columns as rows

emails = df.email.tolist()

# Q4   ------------------

all_domains = map(lambda e: e.split('@')[-1], emails)
len(set(all_domains)) # 4


