year_1 = int(input('Введите год начала отсчёта --> '))
year_2 = int(input('Введите год окончания отсчёта-- > '))
for i in range(year_1, year_2+1):
    if i % 4 == 0:
        print(i, ' - год високосный')
    else:
        print(i, ' - год невисокосный')