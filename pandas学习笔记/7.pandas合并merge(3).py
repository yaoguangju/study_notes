import pandas as pd
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
#indicator=True可以清晰的显示数据是否有,indicator='indicator_column'表示给indicator改个名字
res = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
print(res)
