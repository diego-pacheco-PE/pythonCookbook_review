# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 13:59:35 2021

@author: DIEGO PACHECO
"""
import numpy as np 
# UNPACKING A SEQUENCE INTO SEPARATE VARIABLES

"""
You have an N-element tuple or sequence that you would like 
to unpack into a collection of N variables.
"""
p = (4,5)
x, y = p 
x
y

data = ['ACME', 50, 91.2, (2020,12,21)]
name, quantity, price, mydate = data
print(name)

name, quantity, price,(year, month, day) = data
year

_, var1, var2, _ = data
var1

# UNPACKING ELEMENTS FROM ITERABLES OF ARBITRARY
"""
You need to unpack N elements from an iterable, but the iterable 
may be longer than N elements, causing a 
“too many values to unpack” exception.
"""
# the use of star expressions 

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)

print(drop_first_last([10, 8, 7, 1, 9, 5, 10]))
   
# KEEPING THE LAST N ITEMS
"""
You want to keep a limited history of the last few items seen during iteration
or during some other kind of processing 
"""


import os
print(os.getcwd())
  
from collections import deque
print("ex3")

def search(lines, pattern, history=4):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 4):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
  

 