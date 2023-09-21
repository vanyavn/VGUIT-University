import pandas as pd
sample = pd.read_csv(r'C:\Users\Тома\films.csv')
# из столбца с названием director создадим список (list) - s1
s1 = sample['director'].value_counts().head(3)
print(s1)