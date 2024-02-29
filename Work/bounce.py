# bounce.py
#
# Exercise 1.5

height = 100 # meters
height_reduction = 3/5
i = 1

while i < 11:
    height = height * height_reduction
    i = i+1
    print(i, round(height, 2))
