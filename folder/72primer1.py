import pandas as pd
sample = pd.read_csv(r'C:\Users\Тома\films.csv')
# из столбца с названием создим список (list) - s1
s1 = sample['original_title']
# Каждый элемент списка myList будет представлять название фильма, разбитое на отдельные слова
myList = []
for s in s1:
    myList.append(s.split())
# создаем список из количества слов в каждом названии
xLen=[]
for x in myList:
    xLen.append(len(x))
# а теперь найдем величину и индекс (номер строки в исходной таблице)
# соответствующие максимальному количеству слов
mLen = list(enumerate(xLen,0)) # создать кортеж (значение,индекс)
maxLen = max(mLen, key = lambda i : i[1]) # i[1] - по 2-му индексу, т.е. по значению
# maxLen[0] - индекс (строка) максимума, maxLen[1] - сам максимум
print(maxLen[0],maxLen[1])
print('Фильм, в названии которого больше всего слов')
print(s1[maxLen[0]])