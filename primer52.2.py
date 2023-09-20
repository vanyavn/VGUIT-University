import pandas as pd
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
print('\nИсходный фрейм\n', frame,'\nСписок столбцов:', frame.columns,'. Список индексов:', frame.index,'. Список значений\n', frame.values)
print('Столбец price\n', frame.price,'\nДля строк внутри loc со значением индекса нужной строки\n', frame.loc[2])
print('Выбор нескольких строк указанием массива\n', frame.loc[[2,4]],'\nЧасть фрейма с конкретными строками\n', frame[0:1],'\n\t\tили\n', frame[1:3])
print('Определённое значение из объекта -', frame['object'][3])