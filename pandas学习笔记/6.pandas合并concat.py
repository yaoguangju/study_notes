import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['b','c','d','e'],index=[2,3,4])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])

res = df1.append(s1,ignore_index=True)
res1 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
#join有2种参数，outer表示全部合并，没有数据的用NaN填充，inner(默认)仅仅合并全部有数据的列，其他的全部舍弃
res2 = pd.concat([df1,df2],join='outer',ignore_index=True)
#以df1位标准，将df2上有的数据全部加在df1上
res3 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
#将df2和df3全部加在df1上
res4 = df1.append([df2,df3],ignore_index=True)

print(res1)
print(res2)
print(res3)
print(res4)