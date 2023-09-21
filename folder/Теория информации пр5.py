from math import *
from colorama import Fore
p0_0=p1_1=0.309
p0a_0=p1a_1=p0aa_0=p1aa_1=0.191
p0aaa_0=p1aaa_1=0.15
p0_1=p1_0=0.006
p0a_1=p1a_0=0.017
p0aa_1=p1aa_0=0.044
p0aaa_1=p1aaa_0=0.092
print(Fore.LIGHTYELLOW_EX+'''Исходные данные:\np(0|0) = p(1|1) = 0.309\np(0’|0) = p(1’|1) = 0.191\np(0’’|0) = p(1’’|1) = 0.191\np(0’’’|0) = p(1’’’|1) = 0.15
p(0|1) = p(1|0) = 0.006\np(0’|1) = p(1’|0) = 0.017\np(0’’|1) = p(1’’|0) = 0.044\np(0’’’|1) = p(1’’’|0) = 0.092''')
HY = round((-p0_0*log2(p0_0) - p0a_0*log2(p0a_0) - p0aa_0*log2(p0aa_0) - p0aaa_0*log2(p0aaa_0) - p0_0*log2(p0_0) - p0_0*log2(p0_0) - p0aa_0*log2(p0aa_0)),2)
HYX1 = round((-p0_0*log2(p0_1) - p0a_0*log2(p0a_1)-p0aa_0*log2(p0aa_1) - p0aaa_0*log2(p0aaa_1) - p1_0*log2(p1a_1) - p1aa_0*log2(p1aa_1) - p1aaa_0*log2(p1aaa_1)),2)
C = round((HY - HYX1), 2)
P_err1 = round((p0_1 + p1_0 + p0a_0 + p1_0 + p1aa_1 + p1aa_0 + p0aaa_0 + p0aaa_1),2)
P_err2 = round((p0_1 + p1_0 + p0a_0 + p0a_1),2)
P_err3 = round((p0_1 + p1_0 + p1aa_1 + p1a_0 + p1aa_0 + p1aaa_0 + p0a_1 + p1aa_0),2)
try: HYX0 = -p0_0*log2(1) - p0a_0*log2(p0a_0) - p0aa_0*log2(p0aa_0) - p0aaa_0*log2(p0aaa_0) - p0_0*log2(0) - p0_0*log2(0) - p0a_0*log2(0)
except ValueError:
    print(Fore.LIGHTGREEN_EX+"Задание 1\n"+Fore.LIGHTBLACK_EX+'''Для мягкой демодуляции пропускная способность канала вычисляется по формуле Хартли-Шеннона:
        C = H(Y) - H(Y|X), где H(Y) - энтропия выходных символов, H(Y|X) - условная энтропия выходных символов при заданных входных символах.
Вычислим энтропию выходных символов (H(Y)):
H(Y) = -p(0)log2(p(0)) - p(0’)log2(p(0’)) - p(0’’)log2(p(0’’)) - p(0’’’)log2(p(0’’’)) - p(1’)log2(p(1’)) - p(1’’)log2(p(1’’)) - p(1’’’)log2(p(’’’)) =
     = -0.309log2(0.309) - 0.191log2(0.191) - 0.191log2(0.191) - 0.15log2(0.15) - 0.309log2(0.309) - 0.309log2(0.309) - 0.191log2(0.191)
     ≈ {} бит.'''.format(HY), '''\nH(Y|X=0) = ∞\nH(Y|X=1) ≈ {}\n'''.format(HYX1),'''Так как выдаёт трейсбэк, рассчитаем С через H(Y|X=1).''')
    print(Fore.RED + "H(Y|X=0) невозможно рассчитать (math domain error). Логарифм от нуля не определён!")
    print(Fore.LIGHTBLACK_EX+"Таким образом, пропускная способность для мягкой демодуляции равна:\nC = H(Y) - H(Y|X) = {} бит/символ".format(C)+"\n")
    print(Fore.LIGHTMAGENTA_EX+'Ответ: пропускная способность для мягкой демодуляции приблизительно равна {}, что означает, что данная демодуляция неэффективна для данного канала.'.format(C))
P_err = p0_1 + p1_0
print(Fore.LIGHTGREEN_EX+"Задание 2\n"+Fore.LIGHTBLACK_EX+"Вероятность ошибки декодирования для жесткой демодуляции равна разности P(0|1) и P(1|0)")
print(Fore.LIGHTMAGENTA_EX+"Ответ: вероятность ошибки декодирования для жесткой демодуляции приблизительно равна {}.".format(P_err))
print(Fore.LIGHTGREEN_EX+"Задание 3\n"+Fore.LIGHTBLACK_EX+'''Для демодуляции со стиранием необходимо выбирать наиболее вероятный символ
на выходе из множества (0,1) для каждого входного символа, кроме символов из множества (0’,0’’,0’’’,1’’’,1’’,1’), которые будут проигнорированы.
Таким образом, мы можем рассчитать вероятность ошибки декодирования как сумму вероятностей ошибок для каждого входного символа, за исключением
символов со стиранием: P_err = p(0|1) + p(1|0) + p(0|0’) + p(1|0’) + p(0|0’’) + p(1|0’’’) + p(0|0’’’) + p(1|0’’’) = 0.006 + 0.006 + 0.191 + 0.017
+ 0.191 + 0.044 + 0.15 + 0.092 ≈ {}'''.format(P_err1)+Fore.LIGHTMAGENTA_EX+"\nОтвет: вероятность ошибки декодирования со стиранием приблизительно равна {}.".format(P_err1))
print(Fore.LIGHTGREEN_EX+"Задание 4\n"+Fore.LIGHTBLACK_EX+'''По аналогии с заданием 3. Теперь кроме символов из множества (0,0’,0’’,0’’’,1’’’,1’’,1’,1), которые будут проигнорированы.
Рассчитаем вероятность ошибки декодирования со стиранием: P_err = p(0|1) + p(1|0) + p(0|0') + p(1|0') = 0.006 + 0.006 + 0.191 + 0.017 ≈ {}'''.format(P_err2)+Fore.LIGHTMAGENTA_EX+
"\nОтвет: вероятность ошибки декодирования со стиранием приблизительно равна {}.".format(P_err2))
print(Fore.LIGHTGREEN_EX+"Задание 5\n"+Fore.LIGHTBLACK_EX+'''По аналогии с заданием 3. Теперь кроме символов из множества (0’’’,1’’’), которые будут проигнорированы.
Рассчитаем вероятность ошибки декодирования со стиранием:
P_err = p(0|1) + p(1|0) + p(0|0') + p(1|0') + p(0'|0'') + p(1'|0'') + p(0''|1') + p(1''|1') = 0.006 + 0.006 + 0.191 + 0.017 + 0.044 + 0.092 + 0.017 + 0.044 ≈ {}'''.format(P_err3)+Fore.LIGHTMAGENTA_EX+
"\nОтвет: вероятность ошибки декодирования со стиранием приблизительно равна {}.".format(P_err3))