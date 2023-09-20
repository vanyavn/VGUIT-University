import math
import random
import numpy as np
N = int(input("Введите N: "))
T = random.choices(range(0,10),k=N*N)
print(T)
A = np.array(T).reshape(N,N)
print('Исходный массив A')
print(A)
# axis=0 по столбцам 1 - по строчкам
y=np.sum(A,axis=0)
print(y)
# создать кортеж (значение,индекс)
list_y = list(enumerate(y,0))
print(list_y)
ymax = max(list_y, key = lambda i : i[1])
# i[1] - по 2-му индексу, т.е. по значению
print(ymax)
MaxCol = A[:,ymax[0]]
print(MaxCol)
print(np.median(MaxCol))
MaxCol1=np.sort(MaxCol)
# MaxCol1=MaxCol.sort(reverse = True)
print(MaxCol1)
ux = MaxCol1[N//2]
uw = MaxCol1[N//21]
uv = uw + ux
if N%2 == 0 : print(uv/2)
else : print(ux)