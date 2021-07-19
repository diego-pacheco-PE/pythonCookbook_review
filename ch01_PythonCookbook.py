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
print('-'*20)

# generator function involving yield. 
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
  

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

#  adding or popping items from either end of a queue has O(1) complexity. 

# 1.4 FINDING THE LARGEST OR SMALLEST N ITEMS 
"""
You want to make a list of the largest or smallest N items in a collection 
"""
import heapq

nums = [1,8,2,2,3,6,-7,323,34,1211,3434,12,232,233]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(4,nums))

portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)

#order as a heap
nums = [-2,0,-123,23,2323,54,4,9,-334]
import heapq
heap = list(nums)
#order using heapify! 
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heap)

# 1.5 IMPLEMENTING A PRIORITY QUEUE
"""
You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation. 
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0 

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item: 
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),332)
q.push(Item('spam'),120)
q.push(Item('grok'),5)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
