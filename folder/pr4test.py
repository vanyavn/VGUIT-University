students = {}
f = open('StudentsPerformance.csv')
for line in f:
    info = line.split(',')
    gender = info[0]
    if gender == '"female"':
        print('girls')
        continue
# первая строчка (шапка таблицы) не считается !
    else:
        ethnicity = info[2][1:-1]
        if ethnicity in students:
            students[ethnicity] += 1
        else:
            students[ethnicity] = 1
print(students)


f.close()