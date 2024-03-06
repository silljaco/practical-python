# pcost.py
#
# Exercise 1.27

'''
with open('Data/portfolio.csv', 'rt') as f:
  for line in f:
    print(line, end='')

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',') # next() skips the first line of the table
headers
for line in f:
  row = line.split(',') # split() transforms entries to strings and splits them by ','
  print(row)

f.close()
'''

with open('Data/portfolio.csv', 'rt') as f:
  for line in f:
    print(line, end='')
