import numpy as np
import pandas as pd
a = np.array([1,2,3])
print(a)
a = np.array([[1,2,3],[4,5,6]])
print(a, '\n', a.ndim, '\n', a.shape, '\n', a.dtype)
a = np.array([[1,2,3],[4,5,6]], dtype = float)
print(a.dtype, '\n', a.itemsize, '\n', a.data)
a = np.random.random((2,3))
print(a, '\n', a.sum(), '\n', a.min(), '\n', a.max(), '\n', type(a), '\n', np.zeros((3,3)), '\n', np.ones((3,3)))
w = np.empty((3,3))
print(w, '\n', a)
a=np.arange(5,25,4)
print(a)
a=np.linspace(5,25,5)
print(a)
a = np.logspace(5,25,5)
print(a, '\n', np.sin(a), '\n', np.cos(a), '\n', np.tan(a))
a = np.arange(9).reshape(3,3)
print(a)
a = np.random.random((2,2))
print(a)
b = np.exp([10])
print(b)
b = np.sqrt([16])
print(b)
a = np.array([5, 10, 15, 20, 25])
b = np.array([0, 1, 2, 3, 0])
c = a - b
print(c, '\n', (b**2), '\n', (10 * np.sin(a)), '\n', (a < 15))
a = np.array([[1,1], [0,1]])
b = np.array([[2,0],[3,4]])
print(a*b, '\n', a@b, '\n', a.dot(b))
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8], dtype = float)
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]]) # размерность
df = pd.DataFrame()
x = df.values
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print('arr1 =',arr1, '\narr2 =', arr2, '\n', arr2.dtype, 'размерность arr3\n', np.shape(arr3), '\n', type(x), '\n', my_series.values)
print('одномерный массив из пяти элементов, память для которого выделена, но не инициализирована\n', np.empty(5))
print('массив размером 10x7, заполненный нулями\n', np.zeros((10, 7)))
print('единичная матрица (элементы главной диагонали равны 1, остальные — 0) размера 3х3\n', np.ones((3, 3, 3)))
print('единичная матрица (элементы главной диагонали равны 1, остальные — 0) размера 3х3\n', np.eye(3))
print('массив 3x5 заполненный числом 3.14\n', np.full((3, 5), 3.14))
print('одномерный массив, заполненный числами в диапазоне от 0 до 20 с шагом 7\n', np.arange(0, 21, 7))
print('массив из пяти чисел, равномерно распределѐнных в интервале между 0 и 1 включительно\n', np.linspace(0, 1, 5))
print('массив размера 3х3, заполненный случайными числами из диапазона от 0 до 9 (включительно)\n', np.random.randint(0, 10, (3, 3))) 
my_array = np.array([x for x in range(10)])
print(my_array, '\n', my_array[5], '\n', my_array[-1], '\n', my_array[3:6], '\n', my_array[1:8:3])
my_array = np.array([[1,2,3,4], [10,11,12,13], [45,46,47,48]])
print(my_array, '\n', my_array[1][2]) # 1 строка 2 столбец
students = np.array([[1,135,34,4], [2,160,43,5], [3,163,40,4.3], [4,147,44,5], [5,138,41,4.7]   ])# m * n = 5 * 4
mean = np.mean(students[:,-1])
proverka = (4+5+5+4.3+4.7)/5
median = np.median(students[:,-1]) # [4, 4.3, 4.7, 5, 5] --> типо ученик в середине вот такого столбца если выписать их оценки по иерархии
corr = np.corrcoef(students[:,1], students[:,2])
print(students, '\n', mean, '\nПроверка\n', proverka, '\n', median, corr)