import numpy as np
import math as m
import pandas as pd
from colorama import Fore
def calcI(k, H_AdB, matrix):
    I = k * H_AdB
    df = pd.DataFrame(data = matrix)
    print(Fore.LIGHTGREEN_EX)
    print(df, '\nk =',k,'; Энтропия H(A/B) =', H_AdB,'; I =', I,'.\n\n')
print(Fore.LIGHTMAGENTA_EX+'Задание 1')
matrix1 = np.array([[0,0,1],[0,1,0],[1,0,0]])
h1 = m.log2(matrix1[0][2])+m.log2(matrix1[1][1])+m.log2(matrix1[2][0])
calcI(3, h1, matrix1)
print(Fore.LIGHTMAGENTA_EX+'Задание 2')
matrix2 = np.array([[0.99, 0.01, 0],[0.01, 0.98, 0],[0, 0.01, 1]])
h2 = 1/9*(matrix2[0][0]*m.log2(matrix2[0][0])+matrix2[0][1]*m.log2(matrix2[0][1])+matrix2[1][0]*m.log2(matrix2[1][0])+
      matrix2[1][1]*m.log2(matrix2[1][1])+matrix2[2][1]*m.log2(matrix2[2][1])+matrix2[2][2]*m.log2(matrix2[2][2]))
print(Fore.LIGHTGREEN_EX+'Для H(A/B) мы берём: ',matrix2[0][0],', ',matrix2[0][1],', ',matrix2[1][0],', ',matrix2[1][1],', ',matrix2[2][1],', ',matrix2[2][2])
calcI(6, h2, matrix2)
a, b, c, pba, pab, pac, pca, pcb, pbc = 0.97, 0.97, 0.98, 0.015, 0.02, 0.01, 0.015, 0.01, 0.01
iba,iab,ibc, = -a*pba*m.log2(pba/a), -b*pab*m.log(pab/c), -pbc*c*m.log(pbc/a)
icb,iac,ica = -pac*b*m.log(pac/c), -pac*c*m.log(pac/a), -a*pba*m.log(pba/c)
print(Fore.LIGHTMAGENTA_EX+'Задание 3')
print(Fore.LIGHTGREEN_EX+'Складываем все вероятности\nI(A/B) =',iab,'   I(B/A) =',iba,'   I(B/C) =',ibc,'\nI(C/B) =',icb,'   I(A/C) =',iac,'   I(C/A) =',ica,
      '\nОтвет: I =',iba+iab+ica+iac+ibc+icb, '\n\n')
print(Fore.LIGHTMAGENTA_EX+'Задание 4')
matrix4 = np.array([[0.99, 0.02, 0, 0],[0.01, 0.98, 0.01, 0.01],[0, 0, 0.98, 0.02],[0, 0, 0.01, 0.97]])
ppp = 0.2*0.2*0.2*0.4
h4 = -ppp*(matrix4[0][0]*m.log2(matrix4[0][0])+matrix4[0][1]*m.log2(matrix4[0][1])+matrix4[1][0]*m.log2(matrix4[1][0])+matrix4[1][1]*m.log2(matrix4[1][1])+
           matrix4[1][2]*m.log2(matrix4[1][2])+matrix4[1][3]*m.log2(matrix4[1][3])+matrix4[2][2]*m.log2(matrix4[2][2])+matrix4[2][3]*m.log2(matrix4[2][3])+
           matrix4[3][2]*m.log2(matrix4[3][2])+matrix4[3][3]*m.log2(matrix4[3][3]))
print(Fore.LIGHTGREEN_EX+'Для H(A/B) мы берём: ',matrix4[0][0],', ',matrix4[0][1],', ',matrix4[1][0],', ',matrix4[1][1],', ',matrix4[1][2],', ',
      matrix4[1][3],', ',matrix4[2][2],', ',matrix4[2][3],', ',matrix4[3][2])
df4 = pd.DataFrame(data = matrix4)
print(df4, "\nОтвет:\nH =", h4, "\nP(A/B) =", 1-h4, '\n')
pa, pb, pc = 0.33, 0.33, 0.33
step11, step12 = pa * 0.05, pb * 0.05
step1 = step11 * step12
step2 = 1-(-(step11*step1*m.log2(step1)*9))
print(Fore.LIGHTMAGENTA_EX+'\nЗадание 5'+Fore.LIGHTGREEN_EX+'\npa = ',pa,'; pb =',pb,'; pc =', pc, '.\n',step11, '     ', step12, '    ', step12,'\npa/b =', step1, '\nIa/b =', step2, '\n\n')
print(Fore.LIGHTMAGENTA_EX+'Задание 6')
p_a, p_b, p_c = 0.2, 0.3, 0.5
p_a1_a, p_b1_a, p_c1_a, p_a1_b, p_b1_b, p_c1_b, p_a1_c, p_b1_c, p_c1_c = 0.97, 0.015, 0.015, 0.015, 0.97, 0.015, 0.015, 0.015, 0.97
p_a1 = p_a * p_a1_a + p_b * p_b1_a + p_c * p_c1_a
p_b1 = p_a * p_a1_b + p_b * p_b1_b + p_c * p_c1_b
p_c1 = p_a * p_a1_c + p_b * p_b1_c + p_c * p_c1_c
i_a1 = -m.log2(p_a1)
i_b1 = -m.log2(p_b1)
i_c1 = -m.log2(p_c1)
print(Fore.LIGHTGREEN_EX+'''Рассчитать вероятность каждого сообщения в ансамбле.
Рa = 0,2; Рb = 0,3; Рc = 0,5; Р(а1/а) = Р(b1/b) = P(c1/c) = 0,97; Р(b1/а) = Р(c1/a) = P(a1/b) = Р(c1/b) = Р(a1/c) = P(b1/c) = 0,015.''')
total_info = p_a * i_a1 + p_b * i_b1 + p_c * i_c1
print("I = ", total_info)