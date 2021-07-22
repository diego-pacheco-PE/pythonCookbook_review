import numpy as np 
import pandas as pd

# pd.Series = labeled one-dimension array ... 

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data.values) 

data2 = pd.Series([0.25, 0.5, 0.75, 1], index = ['a', 'b', 'c', 'd']) 
print(data2) 

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict)
print(population['California'])

myarray = np.array(['a','g','f','z'])
print(pd.Series(myarray))

mylist = ['a','g','k','l']
print(pd.Series(mylist))

myarray2 = np.array(['a','g','f','z','s','i','l','o'])
print(pd.Series(myarray2[:7]))

df = pd.read_csv('shift-data.csv')
ser = pd.Series(df['Clock Number'])
print(ser)
print(ser.head(10))

col = pd.Series(df.columns)
print(col)