import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\Тома\tips.csv')
df.head()
df.plot()
plt.show()
df['total_bill'].plot(kind='hist',grid=True,title='Общая сумма счета')
plt.show()
df['day'].value_counts().plot(kind='bar',grid=True,color='darkblue',title='Количество посетителей по дням')
plt.show()
df[['total_bill','tip']].plot(kind='hist',grid=True,subplots=True,title=['Общая сумма счета','Сумма чаевых'],legend=False)
plt.show()
df.plot(x='total_bill',y='tip',kind='scatter',grid=True,title='Общая сумма счета vs Сумма чаевых')
plt.show()
bills_per_day = df['day'].value_counts()
bills_per_day['day']=bills_per_day.index
bmax = df.groupby('day').aggregate(max)
bmin = df.groupby('day').aggregate(min)
bills_per_day['max'] = bmax['total_bill']
bills_per_day['min'] = bmin['total_bill']
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.bar(x= bills_per_day['day'],height=bills_per_day['max'],width = 0.4,align = 'edge',label='Максимальная сумма чека')
axes.bar(x= bills_per_day['day'],height=bills_per_day['min'],width = 0.4,align = 'edge',label='Миниимальная сумма чека')
axes.legend(loc=1)
plt.show()
sns.set()
sns.distplot(df['total_bill'])
plt.show()
sns.pairplot(df)
plt.show()
sns.countplot(x='day',data=df)
plt.show()
sns.boxplot(x='day',y='tip',data=df)
plt.show()
sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
plt.show()