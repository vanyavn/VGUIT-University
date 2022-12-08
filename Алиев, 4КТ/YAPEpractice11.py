import requests
from tkinter import *
from tkinter.messagebox import *
import json
uvu = 'Полуичлось?'
def parsing(): # Будем парсить один из репозиториев гитхаба
    data = {} # Создадим пустой список
    userlink = enter_text.get() # Введённый пользователем юзернейм передаётся переменной userlink
    userlink = "https://api.github.com/users/" + userlink # Конкатенацией строк получаем ссылку
    lol = requests.get(userlink) # GET из Requests получает данные из получившейся ссылки
    kek = lol.json() # Переводим данные в файл JSON
    company, created_at, email, id, name, url = kek['company'], kek['created_at'], kek['email'], kek['id'], kek['name'], kek['url']
    data['company'], data['created_at'], data['email'], data['id'], data['name'], data['url'] = company, created_at, email, id, name, url 
     # Представляем данные, полученные из JSON, в виде словаря
    with open('dataofparsing.json', 'w') as f: # Открывается (или создаётся, если отсутствует) файл json
        json.dump(data, f, indent = 4) # Кодируем словарь в формат JSON с помощью dump
    showinfo(uvu, message = 'Успешно') # Если в терминале нет ошибок и появляется месседжбокс с Успешно, то ошибок нет. Результат в файле :)
okno = Tk() # Работаем с Tkinter и визуализируем данные
okno.title('Алиев Иван, УБ-21')
okno.geometry('579x579')
okno.resizable(0, 0)
okno['bg'] = '#8A2BE2'
enter_text = StringVar()
text_field = Entry(width = 30, insertbackground = '#8A2BE2', fg = '#00ff00', bg = 'black', font = 'Consolas',
 textvariable = enter_text)
text_field.pack(anchor = CENTER)
baton = Button(height = 1, width = 21, text = 'Получить json', bg = '#00ff00', command = parsing)
baton.pack(anchor = CENTER)
okno.mainloop()