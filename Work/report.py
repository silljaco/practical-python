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
    
    ''' 
    ### CREATING TUPLES ###
    for row in rows:
      holding = (row[0], int(row[1]), float(row[2]))
      portfolio.append(holding)
      '''
    
    ### CREATING DICTIONARIES ###
    for row in rows:
      stock = {
        'name' : row[0],
        'shares': int(row[1]),
        'price' : float(row[2])
      }
      portfolio.append(stock)
      
  return portfolio

### Importing the new file: prices.csv ###

import csv



def read_prices(filename):
  
  prices = {}
  
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    
    for row in rows:
      try:
         prices[row[0]] = float(row[1])
      except IndexError:
        pass

  return prices


# filename = input('Enter filename: ') # to enter the filename in the cosolte - not ideal solution
# read_portfolio(filename)
                 
  



