f = open('StudentsPerformance.csv')
magistr = 0
for line in f:
    info = line.split(',')
    gender = info[0]
    if (gender == '"female"'):
        line2=str.replace(line, '"','')
        line3=line2[15:]
        print(line3)
        info2 = line3.split(',')
        edlvl = info2[0]
        if edlvl == "master's degree":
            magistr += 1
print('Девочки с родителями со степенью магистра: {}'.format(magistr))
f.close()