# report.py
#
# Exercise 2.4


import csv

def read_portfolio(filename):
  '''Creates a list of tuples per stockname, amount, price'''
  
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      holding = (row[0], int(row[1]), float(row[2]))
      portfolio.append(holding)
      
      return portfolio


# filename = input('Enter filename: ') # to enter the filename in the cosolte - not ideal solution
# read_portfolio(filename)
                 
  



