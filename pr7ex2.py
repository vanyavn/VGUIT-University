import pandas as pd
df = pd.DataFrame(pd.read_csv(r'C:\Users\Тома\films.csv'))
title, w = df['original_title'], []
for i in range(len(title)): w.append(title[i])
s = set(w)
print(s,'\n',len(s)) # Сколько разных слов используется в названиях фильмов (без учета регистра)?