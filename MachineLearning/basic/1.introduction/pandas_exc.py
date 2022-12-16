import pandas as pd
from IPython.display import display

# 创建关于人的简单数据集
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location' : ["New York", "Paris", "Berlin", "London"],
        'Age' : [24, 13, 53, 33]
       }

data_pandas = pd.DataFrame(data)
# IPython.display可以在Jupyter Notebook中打印出“美观的”DataFrame
display(data_pandas)

