import pandas as pd
df = pd.DataFrame(pd.read_csv(r'C:\Users\Тома\films.csv'))
ye, ac, d = df['release_date'], df['cast'], []
pr = abs(df['revenue']-df['budget'])
for i in range(len(ye)):
    y = str(ye[i])[5:9]
    if y == '2012': d.append(pr[i])
for j in range(len(d)):
    if d[j] == min(d): print('Ответ: ',ac[j]) # Какой актер принес меньше всего прибыли в 2012 году?