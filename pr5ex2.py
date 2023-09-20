import pandas as pd
df = pd.read_csv(r'C:\Users\Тома\football.csv')
print(df)
c = df['Composure'].max()
r = df['Reactions'].max()
x = df[((df['Composure'] > c*0.9) & (df['Reactions'] > r*0.9))]
m = x.Age.min()
print('Ответ -- > ', m, ' лет')