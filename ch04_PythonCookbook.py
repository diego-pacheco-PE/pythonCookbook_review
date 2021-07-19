# 4.1 MANUALLY CONSUMING AN ITERATOR
print("-"*20 +"\n"+ "# 4.1 MANUALLY CONSUMING AN ITERATOR")
"""
You need to process items in an iterable,  but for 
whatever reason, you can't or don't want to use 
loop
"""
with open('somefile.txt') as f:
    try:
        while True: 
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

with open('somefile.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

items = [1,2,3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))

# 4.2 DELEGATING ITERATION
print("-"*20 +"\n"+ "# 4.2 DELEGATING ITERATION")
"""
You have built a custom container object that 
internally holds a list, tuple, or some other 
iterable. 

You would like to make iteration work with your 
new container.
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node): 
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

# 4.3 CREATING NEW ITERATION PATTERNS WITH GENERATORS
print("-"*20 +"\n"+ "# 4.3 CREATING NEW ITERATION PATTERNS WITH GENERATORS")
"""
 You want to implement a custom iteration pattern that’s
 different than the usual builtin functions 
  (e.g., range(), reversed(), etc.).
"""

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0,100,2):
    print(n)

# 4.5 ITERATING IN REVERSE
print("-"*20 +"\n"+ "# 4.5 ITERATING IN REVERSE")
"""
 You want to ITERATE IN A REVERSE OVER A SEQUENCE. 
"""

a = [1,2,3,4,5]

for x in reversed(a):
    print(x)
    