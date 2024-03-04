# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)


### with 1000$ extra payment for the first 12 months

months = 0

while principal > 0
    if months >= 12
        principal = principal * 1+rate/12) - payment - 1000
        total paid = total_paid + payment
    else
         principal = principal * (1+rate/12) - payment
         total_paid = total_paid + payment

print ('Total paid:', total_paid, '$')
