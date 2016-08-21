import re
import csv

with open('faculty.csv', 'r+') as fhand:
  reader = csv.reader(fhand)
  data = [row for row in reader][1:]
  last_names = map(lambda r: r[0].split(' ')[-1], data)
  
  faculty_dict = {}
  for x in range(len(data)):
    if last_names[x] in faculty_dict:
      faculty_dict[last_names[x]].append(tuple(data[x][1:]))
    else:
      faculty_dict[last_names[x]] = [tuple(data[x][1:])]
      
      
  new_dict = {d[0]: d[1:] for d in data}
  
  # sort by last name
  sorted(new_dict.items(), key = lambda tup : tup[0].split(' ')[-1])
