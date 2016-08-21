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

# Without Pandas
import csv
with open('faculty.csv', 'r+') as fhand:
  reader = csv.reader(fhand)
  data = [row for row in reader][1:] # drop header row
  print data

  degrees = map(lambda r: r[1], data)
  # format
  degrees.remove('0')# get rid of the '0' degree
  degrees = map(lambda r: r.replace('.','').strip(), degrees) # get rid of periods
  degrees = map(lambda r: r.split(' '), degrees) # split those with multiple degrees
  unique_degs = set(sum(degrees))
  len(unique_degs) # 8
  
  # value counts
  degs = sum(degrees)
  v_counts = {d: degs.count(d) for d in unique_degs}
  


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



# Q3  & Q4 ------------------

# ...
df.email 
# i'm slightly confused by this section as it seems to be asking me about regex, 
# but even if i weren't using pandas i'd use csv and still just refer to columns as rows

emails = df.email.tolist()


all_domains = map(lambda e: e.split('@')[-1], emails)
len(set(all_domains)) # 4



# without pandas
import re

with open('faculty.csv', 'r+') as fhand:
  data = fhand.read()
  emails = re.findall(r',([a-z1-9]+@.+)\n?', data)
  domains = map(lambda e: e.split('@')[1], emails)
  unique_doms = set(domains)

  print unique_doms # {'cceb.med.upenn.edu', 'email.chop.edu', 'mail.med.upenn.edu', 'upenn.edu'}


