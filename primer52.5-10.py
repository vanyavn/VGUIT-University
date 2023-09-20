import pandas as pd
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
nestdict = {'red': { 2012: 22, 2013: 33 }, 'white': { 2011: 13, 2012: 22, 2013: 16 }, 'blue': { 2011: 17, 2012: 27, 2013: 18 }}
frame, frame2 = pd.DataFrame(data), pd.DataFrame(nestdict)
print('Исходный фрейм\n', frame, '\nПроверить элементы price на то, меньше ли они 1.2 или нет\n', frame[frame['price'] < 1.2])
print('Датафрейм, полученный из словаря\n', frame2, '\nТранспонированный фрейм\n', frame2.T)
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
print('Объекты Index: ', ser.index, '. Методы Index: максимальный - "', ser.idxmax(), '" и минимальный - "', ser.idxmin(), '". Новый экземпляр фрейма')
serd = pd.Series(range(6), index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
print(serd, '\nВывести индексы white\n', serd["white"])
x, y = str(serd.index.is_unique), str(frame.index.is_unique)
print('Проверить индексы на уникальность: у столбца - {0}, у фрейма - {1}.'.format(x,y))