# -*- coding: utf-8 -*-
"""pizza order

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nZUUNOdyEhvSEHp1FI72XBAkQZKXIi1D
"""

print("welcome to pizza Deliveries")
size = input("type 'L'for large 'M' for medium 's' for small:\n")
add_peperoni = input("do u want pepperoni type 'y' for yes and 'n' for no:\n")
extra_cheese = input("do u want extra chees? type 'y' for yes and 'n' for no:\n")
bill = 0
if size == 'L':
  bill += 15
elif size =='M':
  bill += 10
else:
  bill +=7

if add_peperoni =='y':
   if size =="s":
      bill+=3
   else:
      bill+=5

if extra_cheese == 'y':
   if size =='s':
       bill+=2
   else:
      bill+=4


print("enjoy ur Pizza,your final bill is:",bill)