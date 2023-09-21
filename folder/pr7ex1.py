import pandas as pd
data = pd.read_csv(r'C:\Users\Тома\films.csv')
df = pd.DataFrame(data)
mpf = df.query('revenue > budget').groupby(by='director')['director'].count()
print(mpf)
print(*mpf[mpf==mpf.max()].index.tolist()) #У какого из режиссеров самый высокий процент фильмов со сборами выше бюджета?