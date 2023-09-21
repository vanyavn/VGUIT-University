import pandas as pd
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
print('Исходный фрейм\n', frame, '\nОпределим входит ли значение 1.0 в колонку "pen"\n', frame.isin([1.0,'pen']))
print('Заменим, где не входит на NaN', frame[frame.isin([1.0,'pen'])])
frame['new'] = 12
print('С колонкой new\n', frame)
del frame['new']
print('Фрейм после удаления колонки new\n', frame)