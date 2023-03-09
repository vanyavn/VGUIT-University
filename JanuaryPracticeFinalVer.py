from tkinter import *
import requests
import pandas as pd
import matplotlib.pyplot as plt
import ast
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import json
current_day = date.today()
formatted_current_day = datetime.date.strftime(current_day, "%d/%m/%Y") # сегодня
year_ago = date.today()-relativedelta(years=1)
formatted_year_ago = datetime.date.strftime(year_ago, "%d/%m/%Y") # сегодня, но год назад
with open('autosave_dates.json') as f: dates = json.load(f)
datefi, datese = dates['date1'], dates['date2']
with open('autosave_nums.json') as f: nums = json.load(f)
numbers = nums['nums'] # строка
formatted_numbers = ast.literal_eval(numbers) # кортеж
with open('autosave_text.json') as f: autoload_text = json.load(f)
autoload = autoload_text['autoload'] # строка
ws = Tk()
ws.title('Курс валют')
ws.geometry('900x557')
var = StringVar()
def selectLast():
    for elem in formatted_numbers:
        lb.select_set(elem)
def showSelected():
    global cname
    valutes = []
    cname = lb.curselection()
    dname = str(cname)
    ename=', '.join(dname)
    data2={"nums": dname}
    with open('autosave_nums.json','w') as f: json.dump(data2, f)
    stringnew = ''
    for i in cname:
        op = lb.get(i)
        valutes.append(op)
    for val in valutes:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        valcode, numberval, valname = data['Valute'][val]['ID'], data['Valute'][val]['Value'], data['Valute'][val]['Name']
        stringnow = valname+': '+str(numberval)+' рублей. Код: '+valcode
        stringnew += stringnow+'\n' # После закрытия графика
        lab.configure(text='Текущий курс '+valname+': '+str(numberval)+' рублей. Код: '+valcode) # При каждой итерации
        fd,ld,sv = en1.get(), en2.get(),valcode
        data4 = {"date1": fd, "date2": ld}
        with open('autosave_dates.json','w') as f: json.dump(data4, f)
        url2 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={0}&date_req2={1}&VAL_NM_RQ={2}'.format(fd,ld,sv)
        data5 = pd.read_xml(url2)
        val_x=data5["Value"]
        val_l = list(val_x)
        val_a=str(val_l).replace(", ","; ")
        val_b=str(val_a).replace(",",".")
        val_c=str(val_b).replace(";",",")
        val_s=str(val_c)
        val_g = ast.literal_eval(val_s)
        graphvalutes = list(map(float, val_g))
        diapazon=data5["Date"]
        graphdates = list(diapazon)
        x = graphdates
        y = graphvalutes
        fig = plt.figure(figsize=(15,5))
        plt.xticks(rotation=90, fontsize=5.1)
        titleone='Диапазон дат'
        titletwo='Значение курса валют'
        plt.xlabel(titleone, fontsize=11)
        plt.ylabel(titletwo, fontsize=11)
        plt.plot(x,y)
        plt.show()
    autosv=str(valutes)
    data3={"autoload": autosv}
    with open('autosave_text.json', 'w') as f: json.dump(data3, f)
    lab.configure(text='Выбранные текущие курсы валют:\n'+stringnew+'\nСохранено: '+autosv)
showlab = Label(ws, text = "Выберите любое количество валют\nдля построения графика", font = ("Times", 12), padx = 10, pady = 10)
showlab.pack()
lab = Label(ws, text = "Вместо этого текста будут отображены текущие курсы валют. Ваш прошлый выбор сохранён:"+"\n"+autoload, bg='purple')
lab.pack(padx = 20, pady = 19)
date1 = StringVar()
date1.set(datefi)
date2 = StringVar()
date2.set(datese)
def setYearDates():
    date1.set(formatted_year_ago)
    date2.set(formatted_current_day)
def setLastDates():
    date1.set(datefi)
    date2.set(datese)
def selectAll():
    lb.select_set(0, END)
def selectNone():
    lb.select_clear(0, END)

en1 = Entry(ws,width=32, fg = 'green',bg = 'black',font = 'Consolas', insertbackground='#8A2BE2',textvariable = date1)
en1.pack(padx=1, pady=0)
en2 = Entry(ws,width=32, fg= 'green',bg = 'black',font = 'Consolas', insertbackground='#8A2BE2',textvariable = date2)
en2.pack(padx=1, pady=5)
lb = Listbox(ws, selectmode = "multiple")
lb.pack(padx = 10, pady = 10, expand = YES, fill = "both")
valutospisok =["USD","EUR","GBP","JPY","CNY","AZN","AUD","AMD","BYN","BGN","BRL","HUF","HKD","DKK","INR","CAD",
    "KGS","NOK","PLN","RON","XDR","SGD","TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW"]
for item in range(len(valutospisok)):
	lb.insert(END, valutospisok[item]) 
	lb.itemconfig(item, bg="#bdc1d6")
yearbutton=Button(ws, text="Установить даты для годового курса", bg="orange", command=setYearDates).pack()
lastbutton=Button(ws, text="Установить даты прошлого запуска", bg="orange", command=setLastDates).pack()
nonebutton=Button(ws, text="Снять выделение", bg="purple", command=selectNone).pack()
allbutton=Button(ws, text="Выделить все", bg="purple", fg='white', command=selectAll).pack()
numbutton=Button(ws, text="Установить прошлое выделение", bg='purple', fg='green', command=selectLast).pack()
btn=Button(ws, text="Узнать текущий выбранный курс\nПостроить графики для выбранных валют в заданном диапазоне",bg="green",command=showSelected).pack()
selectLast()
ws.mainloop()