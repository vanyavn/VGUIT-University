import numpy as np
import random
import math
N = int(input("Введите M матрицы: "))
M = int(input("Введите N матрицы: "))
T = random.choices(range(0,10),k=M*N)
a = np.array(T).reshape(M,N)
s = np.mean(a)
print('Исходная матрица A:\n', a, '\nСреднее арифметическое матрицы А =', s)
c = 0
dtrmd = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] > s:
            dtrmd.append(a[i][j]) 
            c += 1
otkl=np.std(dtrmd)
print('Количество элементов, больших среднего арифметического =', c, '\nИ это:', dtrmd, '\nА их стандартное отклонение через встроенную функцию\n', otkl)
m = sum(dtrmd) / len(dtrmd)
otkl_res = math.sqrt(sum((xi - m)**2 for xi in dtrmd) / len(dtrmd))
print('И стандартное отклонение через программирование формулы\n',otkl_res)