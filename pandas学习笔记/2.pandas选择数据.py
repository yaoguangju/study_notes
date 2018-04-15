import numpy as np
import pandas as pd
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

#print(df['A'],'\n',df.A)
#print(df[0:3],'\n',df['20130102':'20130104'])
#print(df.loc['20130102']) #以标签的形式选择
#print(df.loc['20130102',['A','B']])  #以标签的形式选择

#print(df.iloc[3:5,1:3]) #以位置进行筛选
#print(df.iloc[[1,3,5],1:3]) #以位置进行筛选

#print(df.ix[:3,['A','C']])  #位置和标签混合进行筛选
print(df[df.A>8]) #条件筛选