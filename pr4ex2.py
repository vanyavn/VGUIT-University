f = open('StudentsPerformance.csv')
math_array, rdscr_array, final = [], [], []
rdscr, w = 0, 0
for line in f:
    info = line.split(',')
    rdscr = info[6] # for reading
    rdscr = rdscr.replace('"','')
    if rdscr == 'reading score':
        rdscr = rdscr.replace('reading score','0')
    numb = int(rdscr)
    rdscr_array.append(numb)
    matm = info[5] # for math
    matm = matm.replace('"','')
    if matm == 'math score':
        matm = matm.replace('math score','0')
    chis = int(matm)
    math_array.append(chis)
mathmax = max(math_array)
print('Максимальный балл по математике: ', mathmax)
maxvals = []
for i in range(len(math_array)):
        if math_array[i] == mathmax:
            maxvals.append(i)
        else: pass
print('Список индексов учеников с максимальным баллом по математике:', maxvals)
for m in range(len(maxvals)):
    l = maxvals[m]
    q = rdscr_array[l]
    final.append(q)
print('Баллы по чтению у учеников с максимальным баллом по математике:', final)
w = sum(final)/len(final)
print('''Ответ -- > Средний балл по чтению у учеников с максимальным баллом по математике,
                    округлённый до 3 знаков после запятой равен:''', round(w, 3))
f.close()