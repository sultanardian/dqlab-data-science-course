import pandas as pd 

df = pd.read_csv('dataset.csv')


print(df.groupby('VisitorType')['Revenue'].count())