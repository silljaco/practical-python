# pcost.py
#
# Exercise 1.27

'''
with open('Data/portfolio.csv', 'rt') as f:
  for line in f:
    print(line, end='')
'''

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
headers
for line in f:
  print(line, end='')
