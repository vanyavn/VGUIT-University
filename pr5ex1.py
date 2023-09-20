import pandas as pd
df = pd.read_csv(r'C:\Users\Тома\football.csv')
people1 = df[(df['Aggression'] == df['Aggression'].max())]
x = round(people1.ShotPower.mean(), 2)
people2 = df[(df['Aggression'] == df['Aggression'].min())]
y = round(people2.ShotPower.mean(), 2)
delta = round(x/y, 2)
print(df, '\nСилы удара игроков с максимальным и минимальным показанием агрессии: ', x, 'и', y, '\nОтвет -- > ', delta)