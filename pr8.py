import pandas as pd
myData = pd.Series([4,11,12,20,23,23,30,31,32,33,34,36,38,40,41,44,44,44,45,47,48,49,54,56])
x = pd.DataFrame(myData).quantile(q=0.5, axis=0, numeric_only=True, interpolation='linear')
x2 = pd.DataFrame(myData).quantile(q=0.5, axis=0, numeric_only=True, interpolation='midpoint')
d, v = [], []
rangee = myData.max() - myData.min()
mean = myData.mean()
var = myData.var()
std = myData.std()
mode = myData.mode()
median = myData.median()
perc25 = myData.quantile(0.25)
perc75 = myData.quantile(0.75)
IQR = perc75 - perc25
for i in range(len(myData)):
    if myData[i] < (perc25 - IQR*1.5): d.append(myData[i])
    elif myData[i] > (perc75 + IQR*1.5): v.append(myData[i])
    else: pass
print(x,'\n',x2,'\nСреднее значение\n',mean,'\nДисперсия\n',var,'\nСтандартное отклонение\n',std,'\nQ1\n',perc25,'\nМедиана (Q2)\n',median,'\nQ3\n',perc75,'\nIQR',IQR,
      '\nМода – наиболее частое наблюдение\n',mode,'\nРазмах\n',rangee,'\nВыбросы\n',d,'\nили\n',v)