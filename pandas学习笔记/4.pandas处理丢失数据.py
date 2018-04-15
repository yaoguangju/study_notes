import numpy as np
import pandas as pd
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

#print(df.dropna(axis=0,how='any')) #how={'any','all'} any只要有就删掉，all当且仅当全部有的话才删除

#print(df.fillna(value=0))  #nan的地方填充数值

print(np.any(df.isnull()) == True) #至少个空值，就可以返回True