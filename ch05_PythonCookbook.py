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

# 5.4 READING AND WRITING BINARY DATA
print("-"*20 +"\n"+ "# 5.4 READING AND WRITING BINARY DATA")

with open('somefile.bin', 'wb') as f:
    f.write(b'hello world?')

with open('somefile.bin', 'rb') as f:
    data = f.read()
    print(data)

    
# 5.5 WRITING TO A FILE THAT DOESNT ALREADY EXIST
print("-"*20 +"\n"+ "# 5.5 WRITING TO A FILE THAT DOESNT ALREADY EXIST")

import os 

if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('hello\n')
else:
        print('file already existS!')


# 5.6 PERFORMING I/O OPERATIONS ON A STRING
print("-"*20 +"\n"+ "# 5.6 PERFORMING I/O OPERATIONS ON A STRING")
"""
You want to feed a text or binary string to code that's
been written to operate on file like objects instead
"""
import io

s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)
print(s.getvalue())

s = io.StringIO('Hello\nWorld\n')
s.read(4)
s.read()

s = io.BytesIO()
s.write(b'Write binary data')
s.getvalue()

""""
The StringIO and BytesIO classes are most useful in scenarios where you need to mimic
a normal file for some reason. For example, in unit tests, you might use StringIO to
create a file-like object containing test data that’s fed into a function that would otherwise
work with a normal file.

Be aware that StringIO and BytesIO instances don’t have a proper integer filedescriptor. 
Thus, they do not work with code that requires the use of a real system-level
file such as a file, pipe, or socket.
"""
# 5.7 READING AND WRITING COMPRESSED DATAFILES
print("-"*20 +"\n"+ "# 5.7 READING AND WRITING COMPRESSED DATAFILES")
"""
You need to read or write data in a file with gzip or bz2 compression
"""
import gzip 
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

import bz2 
with bz2.open('somefile.bz2', 'rt') as f: 
    text = f.read()

import gzip 
with gzip.open('somefile.gz', 'wt') as f:
    f.write("fooo text")

import bz2 
with bz2.open('somefile.bz2', 'wt') as f:
    f.write("fooo text")