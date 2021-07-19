# 5.1 READING AND WRITING TEXT DATA
print("-"*20 +"\n"+ "# 5.1 READING AND WRITING TEXT DATA")
"""
You need to read or write text data, possibly in
different text encodings such as ASCII, utf8 or utf16.
"""

with open('somefile.txt', 'rt') as f:
    data = f.read()
print(data)

with open('somefile.txt', 'wt') as f:
    print("199python", file=f)
    print("200python", file=f)
    print("299python", file=f)
    
with open('somefile.txt', 'at') as f:
    print("Xpython", file=f)
    print("Ypython", file=f)
    print("Zpython", file=f)

with open('somefile.txt', 'rt') as f:
    data = f.read()
print(data)

#with open('somefile.txt', 'rt') as f:
#    for line in f: 
        # process some line

# encoding by default 
import sys
print(sys.getdefaultencoding())

# without with keyword 
f = open('somefile.txt', 'rt')
data = f.read()
print("-"*20 +"\n"+ "Sin usar with...." + "\n" + data)
f.close()

# 5.2 PRINTING TO A FILE
print("-"*20 +"\n"+ "# 5.2 PRINTING TO A FILE")

"""
You want to redirect the output of print() function
to a file
"""

with open('somefile.txt','wt') as f:
    print('hello world!...', file=f)

f = open('somefile.txt', 'rt')
data = f.read() 
print(data)
f.close()

# 5.3 PRINTING WITH A DIFFERENTE SEPARATOR 
# OR LINE ENDING
print("-"*20 +"\n"+ "# 5.3 PRINTING WITH A DIFFERENTE SEPARATOR OR LINE ENDING")

print('ACME', 50, 98.3)
print('JMIA',49,2.2, sep = ',')
print('RDO', 23, 4.22, sep = ',', end = '!!\n')
for i in range(12):
    print(i, end = ' ')
print('\n')
for i in range(12):
    print(i)

mytup1 = ('APPL','Apple mechanic',str(23.42))
mytup2 = ('APPL', 34.2, 34039.3)
print(";".join(mytup1)) 
print(*mytup2, sep=';')

