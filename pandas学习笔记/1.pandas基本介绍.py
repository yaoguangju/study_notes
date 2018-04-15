import numpy as np
import pandas as pd
s = pd.Series([1,3,6,np.nan,44,1])
#print(s)
dates = pd.date_range('20160101',periods=6)
#print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d']) #index是列标，columns是行标
#print(df)
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
#print(df1)
df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
#print(df2)
#print(df2.dtypes) #输出每列的数据类型
#print(df2.columns) #输出列标
#print(df2.values) #输出所有数据值
#print(df2.T) #输出转置
#print(df2.sort_index(axis=1,ascending=False)) #输出按列排序的逆序
#print(df2.sort_index(axis=0,ascending=False)) #输出按行排序的逆序
print(df2.sort_values(by='E')) #输出按照E这一行的排序