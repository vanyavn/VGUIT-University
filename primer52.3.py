import pandas as pd
import numpy as np
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame.index.name = 'id'
frame.columns.name = 'item'
print('Исходный фрейм\n', frame)
frame['new'] = 12
print('Добавление нового столбца\n', frame['new'])
frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]
print('Изменение нового столбца\n', frame['new'])
ser = pd.Series(np.arange(5))
frame['new'] = ser
x = 3.3
del frame['price'][2]
frame['price'][2] = x
print('Присвоение значений от 0 до 4 экземпляру датафрейма new и замена значениия price второй строки на 3.3\n', frame)