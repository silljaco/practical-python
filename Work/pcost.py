# pcost.py
#
# Exercise 1.27

'''
with open('Data/portfolio.csv', 'rt') as f:
  for line in f:
    print(line, end='')
'''

'''
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',') # next() skips the first line of the table
headers
for line in f:
  row = line.split(',') # split() transforms entries to strings and splits them by ','
  print(row)

f.close()
'''


import csv
def portfolio_cost(filename):
  total_cost = 0.0
  
  with open(filename, 'rt')as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      nshares = int(row[1])
      price = float(row[2])
      total_cost += nshares * price
  return total_cost

filename = input('Enter filename')

cost = portfolio_cost(filename)
print('Total cost:', cost)



    

