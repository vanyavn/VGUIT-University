from tkinter import *
import requests
import pandas as pd
import matplotlib.pyplot as plt
import ast
import datetime
from datetime import date
from datetime import timedelta
import random
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
    lb.select_clear(0, END)
    for elem in formatted_numbers:
        lb.select_set(elem)
def showSelected():
    global cname
    valutes = []
    cname = lb.curselection()
    dname = str(cname)
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
        stringnew += stringnow+'\n' # после закрытия графика
        lab.configure(text='Текущий курс '+valname+': '+str(numberval)+' рублей. Код: '+valcode) # при каждой итерации
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
lab = Label(ws, text = "Вместо этого текста будут отображены текущие курсы валют. Ваш прошлый выбор сохранён:"+"\n"+autoload, bg='#FFBD00')
lab.pack(padx = 20, pady = 19)
date1 = StringVar()
date1.set(datefi)
date2 = StringVar()
date2.set(datese)
def setRandomDates():
    min_year=1999
    max_year = date.today().year
    startingdate = date(min_year, 1, 1)
    yeardistance = max_year - min_year+1
    endingdate = startingdate + timedelta(days=365 * yeardistance)
    rands=''
    for k in range(2):
        randtime = startingdate + (endingdate - startingdate) * random.random()
        gentime = str(randtime)
        ragt = gentime[0:10]
        ragt_yyyy=ragt[0:4]
        ragt_mm=ragt[5:7]
        ragt_dd=ragt[8:10]
        newrandom1=ragt_dd+'/'+ragt_mm+'/'+ragt_yyyy
        rands+=newrandom1
    randate1=rands[0:10]
    randate2=rands[10:20]
    date1.set(randate1)
    date2.set(randate2)
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
en1 = Entry(ws,width=32, fg = '#00ff00',bg = 'black',font = 'Consolas', insertbackground='#8A2BE2',textvariable = date1)
en1.pack(padx=1, pady=0)
en2 = Entry(ws,width=32, fg= '#00ff00',bg = 'black',font = 'Consolas', insertbackground='#8A2BE2',textvariable = date2)
en2.pack(padx=1, pady=5)
lb = Listbox(ws, selectmode = "multiple")
lb.pack(padx = 10, pady = 10, expand = YES, fill = "both")
valutospisok =["USD","EUR","GBP","JPY","CNY","AZN","AUD","AMD","BYN","BGN","BRL","HUF","HKD","DKK","INR","CAD",
    "KGS","NOK","PLN","RON","XDR","SGD","TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW"]
for item in range(len(valutospisok)):
	lb.insert(END, valutospisok[item]) 
	lb.itemconfig(item, bg="#FF7514")
yearbutton = Button(ws, text="Установить даты для годового курса", bg="#00ff00", command=setYearDates).pack()
lastbutton = Button(ws, text="Установить даты прошлого запуска", bg="#00ff00", command=setLastDates).pack()
randombutton = Button(ws, text="Установить рандомные даты", bg="#00ff00", command=setRandomDates).pack()
nonebutton = Button(ws, text="Снять выделение", bg="#00ff00", command=selectNone).pack()
allbutton = Button(ws, text="Выделить все", bg="#00ff00", command=selectAll).pack()
numbutton = Button(ws, text="Установить прошлое выделение", bg="#00ff00", command=selectLast).pack()
btn = Button(ws, text="Узнать текущий выбранный курс\nПостроить графики для выбранных валют в заданном диапазоне", bg="#9400d3", command = showSelected).pack()
selectLast()
ws.mainloop()