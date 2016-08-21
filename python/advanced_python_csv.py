import re

data = None
emails = None
domains = None
unique_doms = None

with open('faculty.csv', 'r+') as fhand:
  data = fhand.read()
  emails = re.findall(r',([a-z1-9]+@.+)\n?', data)
  domains = map(lambda e: e.split('@')[1], emails)
  unique_doms = set(domains)

with open('emails.csv', 'w+') as f:
  for e in emails:
    f.write(e + '\n')

