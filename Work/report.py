# report.py
#
# Exercise 2.4


import csv

def portfolio_cost(filename):
  '''Calculates the total cost (shares*price) of a portfolio file'''
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      holding = (row[0], int(row[1]), float(row[2]))
      portfolio.append(holding)
      
      return portfolio
                 
  



