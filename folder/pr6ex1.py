import numpy as np
import random
def mediana(x: list) -> float:
    n = len(x)
    t = sorted(x)
    if n % 2 == 1:
        return t[n // 2]
    else:
        return 0.5 * (t[n//2] + t[n//2-1])
j, x = [], []
mn, mi = 0, 0
N = int(input("Введите N: "))
T = random.choices(range(0,10),k=N*N)
print(T)
A = np.array(T).reshape(N,N)
print('Исходная квадратная матрица A\n', A)
for i in range(N):
    p = sum(A[:,i])
    print('Сумма элементов',i,'-го столбца =',p)
    j.append(p)
mn = np.where(j == np.min(j))[0]
print(mn)
mi = mn[0]
print('Список сумм столбцов исходного массива:',j,'\nИндекс элемента с минимальным значением столбца:', mi, '\nИскомый столбец', A[:,mi])
x = A[:,mi]
median = np.median(A[:,mi])
print('Ответ через стандартной функцию. Медиана равна ', median,'\nОтвет программированием функции. Медиана равна', mediana(x))