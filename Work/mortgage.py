# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

''' multiline comment to cut out example code

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
'''

### with 1000$ extra payment for the first 12 months

months = 1

while principal > 0 and months <= 12:
        principal = principal * (1+rate/12) - payment - 1000
        total_paid = total_paid + payment + 1000
        months = months + 1

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months +1

print ('Total paid:', round(total_paid, 2), '$')
print ('In', months, 'months')
