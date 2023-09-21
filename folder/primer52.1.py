import pandas as pd
import numpy as np
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'], 'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'], 'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame2 = pd.DataFrame(data, columns=['object', 'price'])
frame3 = pd.DataFrame(np.arange(16).reshape((4,4)), index = ['red', 'blue', 'yellow', 'white'], columns = ['ball', 'pen', 'pencil', 'paper'])
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame([ [1,2,3], [2,3,4] ], columns = ['foo', 'bar', 'baz'], index = ['foobar', 'foobaz'])
print('Словарь во фрейм\n', frame, '\nСоздание фрейма\n', frame2, '\nПрисвоение меток\n', frame3, '\nСловарь со списками во фрейм\n', df, '\nСписки во фрейм\n', df2)