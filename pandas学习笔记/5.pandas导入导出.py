import pandas as pd
    data = pd.read_csv('student.csv') #导入
    print(data)

    data.to_pickle('student.pickle') #导出