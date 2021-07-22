import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame

ef1 = 'shift-data.xlsx'
ef2 = 'third-shift-data.xlsx'

df_first_shift = pd.read_excel(ef1, sheet_name='first')
df_second_shift = pd.read_excel(ef1, sheet_name='second')
df_third_shift = pd.read_excel(ef2)

df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
df_all.info()
print(df_all)

pivot = df_all.groupby(['Shift']).mean()
shift_productivity = pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]
print(shift_productivity)
 
shift_productivity.plot(kind='bar')
# plt.show()

import pandas as pd 
series1 = pd.Series([10,20,30])
series2 = pd.Series(['Kavi', 'Shyan','Singh'],index=[3,9,1])
series3 = pd.Series([4,6,12], index=['Caceres','Miglioti','Da Souza'])
print(series1)
print(series2)
print(series3)

ar = np.array([1,6,2])
series4 = pd.Series(ar, index = ['Jan','Feb','Mar'])
print(series4)

dict1 = {'India':'New Delhi', 'UK':'London', 'Peru':'Lima'}
series5 = pd.Series(dict1)
print(series5)
print('*'*30)
print(series5[0])
print('*'*30)
print(series5['Peru'])
print('*'*30)
print(series5[[0,1,2]])
print('*'*30)
print(series5[['UK','Peru']])
print('*'*30)
print(series5[0:3]) #excludes the value at index position 3.
print('*'*30)
print(series5.size)
print('*'*30)
print(series5.head(2))
print(series5.count())
print(series5.tail(2))

seriesA = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
seriesB = pd.Series([10,20,30,40,50], index = ['a','b','c','g','f'])
seriesC = seriesA + seriesB
print(seriesC)
print(seriesA.add(seriesB, fill_value=0))

import pandas as pd 
df = pd.DataFrame()
print(df)

import numpy as np
array1 = np.array([1,2,3,4])
array2 = np.array([4,3,2,1])
array3 = np.array(['Diego','Seba','Nelly','Kelly'])

df = pd.DataFrame([array1, array2, array3],columns=['A','B','C','D'])
print(df)