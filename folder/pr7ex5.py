import pandas as pd
df = pd.DataFrame(pd.read_csv(r'C:\Users\Тома\films.csv'))
ye, re, w = df['release_date'], df['director'], []
for i in range(len(ye)):
    y = str(ye[i]).split('/')
    if y[0] in ('1','2','12'):
        w.append(re[i])
        print(y[0])
print(max(set(w), key=lambda x: w.count(x))) # Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?