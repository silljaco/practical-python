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

total_cost = 0.0

def portfolio_cost(filname):
  with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost += nshares * price
    return total_cost
    print('Total cost', total_cost)
      
cost = portfolio_cost('/Data/portfolio.csv')

