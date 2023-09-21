import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(pd.read_csv(r'C:\Users\Тома\films.csv'))
df = df.assign(profit = df.revenue - df.budget) # Добавляет новый столбец в дф, содержащий разницу между сборами и бюджетом
re, rd, pr, lst, count_dict, new, new2, x, y = df["director"].tolist(), df["release_date"].tolist(), df["profit"].tolist(), [], {}, [], [], [], []
for i in range(len(df.profit)):
    if pr[i] > 0: lst.append(re[i]) # Если сборы у строки дф больше бюджета (профит больше нуля) в список 'lst' добавляется i-ый элемент
for item in lst:
    if item in count_dict: count_dict[item] += 1
    else: count_dict[item] = 1
sorted_lst = sorted(lst, key=lambda x: count_dict[x], reverse = True) # Функция подсчёта фильмов у режиссёра
for item in sorted_lst:
    print(item, count_dict[item])
    new.append(item) # Список имён режиссёров
    new2.append(count_dict[item]) # Список с количествами повторений режиссёров (количество фильмов)# Как это выглядит вместе
cool_dict, cool_dict2 = dict(zip(new, new2)), dict(zip(new2, new)) # Делаем словарь из режиссёров и их количества фильмов
keys, keys2 = list(cool_dict.keys()), list(cool_dict2.keys())
for r in range(0, 10): x.append(keys[r]) # Мы получили топ-10 режиссёров
for a in range(0, 10): y.append(keys2[a])
print('Исходный фрейм:\n', df, '\nСловарь режиссёров:\n', cool_dict, '\nТоп-10 режиссёров:', x, '\nКоличество их фильмов:', y, cool_dict, keys2) 
plt.bar(x, y) # Мы получили данные для осей абсцисс и ординат для последующей визуализации данных
plt.title("Технология защищённой обработки больших данных\nПрактическая работа №9.1(В-1)\nВыполнил Алиев И.\nПоставьте 85+\n:) Пойду на дата саенс :)", fontsize = 9, color = 'm')
plt.xlabel("Режиссёры", fontsize=11)
plt.xticks(rotation=0, fontsize=7)
plt.ylabel("Количество их фильмов", fontsize=11)
plt.show()