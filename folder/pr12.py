import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import skew, kurtosis
import seaborn as se
import pingouin as pg
import skidmarks as sk
from colorama import Fore
df = pd.read_csv(r'C:/Users/Тома/Rent.csv',sep=';')
z,x,c,r,w,d = list(sorted(df['rent'])),list(sorted(df['s'])),list(sorted(df['floor'])),list(sorted(df['rooms'])),list(sorted(df['walls'])),list(sorted(df['district']))
u = pd.DataFrame([z,x,c,r,w,d])
i = df.dtypes
plt.title('Задание 4 - 5. Визуализизация данных',color='purple')
plt.xlabel('Аренда',color='purple')
plt.ylabel('Стоимость',color='purple')
plt.fill_between(z, x, np.zeros_like(d), color='darkorchid') 
vis=plt.plot(z, x, color = 'darkviolet')
plt.show()
zzz = stats.normaltest(z)
ddd = stats.normaltest(d)
koas = skew(z,axis=0,bias=True)
koax = kurtosis(z,axis=0,bias=True)
print(Fore.MAGENTA+'Задание 1')
print(Fore.GREEN+'\nДанные подгрузил\n',df)
print(Fore.MAGENTA+'\n\nЗадание 2.Структурирование данных:\n')
print(Fore.GREEN+'',u) # 0-i, 1-koas
print(Fore.MAGENTA+'\nЗадание 3. Анализ типов данных:')
print(Fore.GREEN+'\n',i)
print(Fore.MAGENTA+'Задние 5\n')
print(Fore.GREEN+'\nКоэффициент асимметрии:\n',koas,'\nКоэффициент эксцесса:\n',koax)
print(Fore.MAGENTA+'\nЗадние 6. Тест д.Агостино:\n'+Fore.GREEN+'\n',zzz,'\n',ddd)
dd,zz = str(d), str(z)
print(Fore.MAGENTA+'Задание 7\n'+Fore.GREEN+'')
st1, st2, st3, st4 = 'Это количественные данные!','Это не количественные данные!','Данные нормальные!','Данные не нормальные!'
st5, st6, st7, st8 = 'Порядковые данные!','Качестенные данные!','1) Зависимые.','2) Зависимые.'
if (zz.isdigit()==True) and (dd.isdigit()==True): print(st1)
else: print(st2)
if (st2==True) and (st1==True): print(st3)
else: print(st4)
lst = [z, d]
if len(lst)==2: print(stats.ttest_ind(a=z,b=d))
else: print(pg.welch_anova(dv='rent',between='district',data=df))
e1,r1=list(df['rent']),list(df['district'])
if (st2==True) and (e1!=z) and (r1!=d): print(st5)
else: print(st6)
if st6==True: print('Хи-квадрат; точный критерий фишера и другое:\n\n',stats.chisquare(f_obs=z,f_exp=d),'\n\n',stats.chisquare(f_obs=d,f_exp=z),'\n\n',
                    stats.fisher_exact(z),'\n\n',stats.fisher_exact(d))
if (st5 == True) and (st4 == True) and (len(lst) == 2): print(st7)
else:
    if (st7 == True) and (np.corrcoef(z,d) > 2): print(st8,'\n',stats.wilcoxon(z,d))
    elif (st7 == True) and (np.corrcoef(z,d) <= 2): print(sk.wald_wolfowitz(z),'\n\n',sk.wald_wolfowitz(d),'\n\n',stats.ks_2samp(z,d),'\n\n',stats.mannwhitneyu(z,d))
    elif (st8 == True) and (np.corrcoef(z,d) >= 2): print(stats.friedmanchisquare(z,d))
    else: print(stats.kruskal(z,d))
f1_0, f1_1, f2_0, f2_1 = 0, 0, 0, 0
rentlst, distlst = df['rent'].tolist(), df['district'].tolist()
for ll in range(len(rentlst)):
    if rentlst[ll] == 0: f1_0 += 1
    else: f1_1 += 1
for hh in range(len(distlst)):
    if distlst[hh] == 1: f2_0 += 1
    else: f2_1 += 1
print(f1_0, f1_1, f2_0, f2_1)
newf1, newf2 = [f1_0, f1_1], [f2_0, f2_1]
print(Fore.MAGENTA+'Задание 8\n')
print(Fore.GREEN+'Проверка по парному критерию Манна-Уитни:\n\n',stats.mannwhitneyu(newf1, newf2, method="asymptotic"))
print(Fore.MAGENTA+'Задание 9. Визуализировал\n')
sns = se.jointplot(z,kind="reg",color="purple")
plt.show()
sns = se.jointplot(x,kind="reg",color="purple")
plt.show()