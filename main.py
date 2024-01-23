import pandas as pd

data = pd.read_csv('cleaned_data.csv', delimiter=',')
df = pd.DataFrame(data)

print(df.head(15))
print(df.shape) # (35468, 1)
print(df.dtypes)

row = df.iloc[0:1]
row2 = df.iloc[1:2]
row.to_excel('row.xlsx', index='False')
row2.to_excel('row2.xlsx', index='False')
df.to_excel('data.xlsx', index='False')
