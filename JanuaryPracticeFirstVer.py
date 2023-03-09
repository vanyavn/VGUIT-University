from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox, ttk, Tk
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import ast
import json
current_day = date.today()
formatted_current = datetime.date.strftime(current_day, "%d/%m/%Y") # Сегодня
year_ago = date.today()-relativedelta(years=1)
formatted_ya = datetime.date.strftime(year_ago, "%d/%m/%Y") # Сегодня, но год назад
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
usd, x_usd, y_usd = data['Valute']['USD']['Value'], data['Valute']['USD']['Name'], data['Valute']['USD']['ID']
eur, x_eur, y_eur = data['Valute']['EUR']['Value'], data['Valute']['EUR']['Name'], data['Valute']['EUR']['ID']
gbp, x_gbp, y_gbp = data['Valute']['GBP']['Value'], data['Valute']['GBP']['Name'], data['Valute']['GBP']['ID']
jpy, x_jpy, y_jpy = data['Valute']['JPY']['Value'], data['Valute']['JPY']['Name'], data['Valute']['JPY']['ID']
cny, x_cny, y_cny = data['Valute']['CNY']['Value'], data['Valute']['CNY']['Name'], data['Valute']['CNY']['ID']
azn, x_azn, y_azn = data['Valute']['AZN']['Value'], data['Valute']['AZN']['Name'], data['Valute']['AZN']['ID']
aud, x_aud, y_aud = data['Valute']['AUD']['Value'], data['Valute']['AUD']['Name'], data['Valute']['AUD']['ID']
amd, x_amd, y_amd = data['Valute']['AMD']['Value'], data['Valute']['AMD']['Name'], data['Valute']['AMD']['ID']
byn, x_byn, y_byn = data['Valute']['BYN']['Value'], data['Valute']['BYN']['Name'], data['Valute']['BYN']['ID']
bgn, x_bgn, y_bgn = data['Valute']['BGN']['Value'], data['Valute']['BGN']['Name'], data['Valute']['BGN']['ID']
brl, x_brl, y_brl = data['Valute']['BRL']['Value'], data['Valute']['BRL']['Name'], data['Valute']['BRL']['ID']
huf, x_huf, y_huf = data['Valute']['HUF']['Value'], data['Valute']['HUF']['Name'], data['Valute']['HUF']['ID']
hkd, x_hkd, y_hkd = data['Valute']['HKD']['Value'], data['Valute']['HKD']['Name'], data['Valute']['HKD']['ID']
dkk, x_dkk, y_dkk = data['Valute']['DKK']['Value'], data['Valute']['DKK']['Name'], data['Valute']['DKK']['ID']
inr, x_inr, y_inr = data['Valute']['INR']['Value'], data['Valute']['INR']['Name'], data['Valute']['INR']['ID']
cad, x_cad, y_cad = data['Valute']['CAD']['Value'], data['Valute']['CAD']['Name'], data['Valute']['CAD']['ID']
kgs, x_kgs, y_kgs = data['Valute']['KGS']['Value'], data['Valute']['KGS']['Name'], data['Valute']['KGS']['ID']
nok, x_nok, y_nok = data['Valute']['NOK']['Value'], data['Valute']['NOK']['Name'], data['Valute']['NOK']['ID']
pln, x_pln, y_pln = data['Valute']['PLN']['Value'], data['Valute']['PLN']['Name'], data['Valute']['PLN']['ID']
ron, x_ron, y_ron = data['Valute']['RON']['Value'], data['Valute']['RON']['Name'], data['Valute']['RON']['ID']
xdr, x_xdr, y_xdr = data['Valute']['XDR']['Value'], data['Valute']['XDR']['Name'], data['Valute']['XDR']['ID']
sgd, x_sgd, y_sgd = data['Valute']['SGD']['Value'], data['Valute']['SGD']['Name'], data['Valute']['SGD']['ID']
tjs, x_tjs, y_tjs = data['Valute']['TJS']['Value'], data['Valute']['TJS']['Name'], data['Valute']['TJS']['ID']
tryv, x_tryv, y_tryv = data['Valute']['TRY']['Value'], data['Valute']['TRY']['Name'], data['Valute']['TRY']['ID']
tmt, x_tmt, y_tmt = data['Valute']['TMT']['Value'], data['Valute']['TMT']['Name'], data['Valute']['TMT']['ID']
uzs, x_uzs, y_uzs = data['Valute']['UZS']['Value'], data['Valute']['UZS']['Name'], data['Valute']['UZS']['ID']
uah, x_uah, y_uah = data['Valute']['UAH']['Value'], data['Valute']['UAH']['Name'], data['Valute']['UAH']['ID']
czk, x_czk, y_czk = data['Valute']['CZK']['Value'], data['Valute']['CZK']['Name'], data['Valute']['CZK']['ID']
sek, x_sek, y_sek = data['Valute']['SEK']['Value'], data['Valute']['SEK']['Name'], data['Valute']['SEK']['ID']
chf, x_chf, y_chf = data['Valute']['CHF']['Value'], data['Valute']['CHF']['Name'], data['Valute']['CHF']['ID']
zar, x_zar, y_zar = data['Valute']['ZAR']['Value'], data['Valute']['ZAR']['Name'], data['Valute']['ZAR']['ID']
krw, x_krw, y_krw = data['Valute']['KRW']['Value'], data['Valute']['KRW']['Name'], data['Valute']['KRW']['ID']
with open('dataforautosave.json') as f:
    data4 = json.load(f)
svalth,datefi,datese=data4['svalth'],data4['datefi'],data4['datese']
with open('asl1.json') as f:
    data41 = json.load(f)
svalfi = data41['svalfi']
with open('asl2.json') as f:
    data42 = json.load(f)
svalse = data42['svalse']
window = Tk()
window.title("Январьская практика, ИЗ№3, Ваня Алиев. Курс валют. Приложение с графиком :)")
window.geometry("1000x500")
date1 = StringVar()
date1.set(datefi)
date2 = StringVar()
date2.set(datese)
first_sel = IntVar()
second_sel = IntVar()
third_sel = IntVar()
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Текущие")
tab_control.add(tab2, text = "За год")
tab_control.add(tab3, text = "За определённый промежуток")
tab_control.pack(expand = 1, fill = 'both')
yav = str()
xav = str()
def av(): # all valutes
    global first_sel
    if combo.get() == "USD": vwa, first_sel, vwb, vwc = x_usd, 0, y_usd, usd
    elif combo.get() == "EUR": vwa, first_sel, vwb, vwc = x_eur, 1, y_eur, eur
    elif combo.get() == "GBP": vwa, first_sel, vwb, vwc = x_gbp, 2, y_gbp, gbp
    elif combo.get() == "JPY": vwa, first_sel, vwb, vwc = x_jpy, 3, y_jpy, jpy
    elif combo.get() == "CNY": vwa, first_sel, vwb, vwc = x_cny, 4, y_cny, cny
    elif combo.get() == "AZN": vwa, first_sel, vwb, vwc = x_azn, 5, y_azn, azn
    elif combo.get() == "AUD": vwa, first_sel, vwb, vwc = x_aud, 6, y_aud, aud
    elif combo.get() == "AMD": vwa, first_sel, vwb, vwc = x_amd, 7, y_amd, amd
    elif combo.get() == "BYN": vwa, first_sel, vwb, vwc = x_byn, 8, y_byn, byn
    elif combo.get() == "BGN": vwa, first_sel, vwb, vwc = x_bgn, 9, y_bgn, bgn
    elif combo.get() == "BRL": vwa, first_sel, vwb, vwc = x_brl, 10, y_brl, brl
    elif combo.get() == "HUF": vwa, first_sel, vwb, vwc = x_huf, 11, y_huf, huf
    elif combo.get() == "HKD": vwa, first_sel, vwb, vwc = x_hkd, 12, y_hkd, hkd
    elif combo.get() == "DKK": vwa, first_sel, vwb, vwc = x_dkk, 13, y_dkk, dkk
    elif combo.get() == "INR": vwa, first_sel, vwb, vwc = x_inr, 14, y_inr, inr
    elif combo.get() == "CAD": vwa, first_sel, vwb, vwc = x_cad, 15, y_cad, cad
    elif combo.get() == "KGS": vwa, first_sel, vwb, vwc = x_kgs, 16, y_kgs, kgs
    elif combo.get() == "NOK": vwa, first_sel, vwb, vwc = x_nok, 17, y_nok, nok
    elif combo.get() == "PLN": vwa, first_sel, vwb, vwc = x_pln, 18, y_pln, pln
    elif combo.get() == "RON": vwa, first_sel, vwb, vwc = x_ron, 19, y_ron, ron
    elif combo.get() == "XDR": vwa, first_sel, vwb, vwc = x_xdr, 20, y_xdr, xdr
    elif combo.get() == "SGD": vwa, first_sel, vwb, vwc = x_sgd, 21, y_sgd, sgd
    elif combo.get() == "TJS": vwa, first_sel, vwb, vwc = x_tjs, 22, y_tjs, tjs
    elif combo.get() == "TRY": vwa, first_sel, vwb, vwc = x_tryv, 23, y_tryv, tryv
    elif combo.get() == "TMT": vwa, first_sel, vwb, vwc = x_tmt, 24, y_tmt, tmt
    elif combo.get() == "UZS": vwa, first_sel, vwb, vwc = x_uzs, 25, y_uzs, uzs
    elif combo.get() == "UAH": vwa, first_sel, vwb, vwc = x_uah, 26, y_uah, uah
    elif combo.get() == "CZK": vwa, first_sel, vwb, vwc = x_czk, 27, y_czk, czk
    elif combo.get() == "SEK": vwa, first_sel, vwb, vwc = x_sek, 28, y_sek, sek
    elif combo.get() == "CHF": vwa, first_sel, vwb, vwc = x_chf, 29, y_chf, chf
    elif combo.get() == "ZAR": vwa, first_sel, vwb, vwc = x_zar, 30, y_zar, zar
    elif combo.get() == "KRW": vwa, first_sel, vwb, vwc = x_krw, 31, y_krw, krw
    label1.configure(text=str(vwc)+' рублей'+'\n'+vwa+'\n'+'Код:'+vwb)
    data41={"svalfi": first_sel}
    with open('asl1.json', 'w') as f:
        json.dump(data41, f)
def uv(): # for ya graph
    global yav, formatted_ya, formatted_current, second_sel
    if combo2.get() == "USD": ybv, second_sel, yav = x_usd, 0, y_eur
    elif combo2.get() == "EUR": ybv, second_sel, yav = x_eur, 1, y_eur
    elif combo2.get() == "GBP": ybv, second_sel, yav = x_gbp, 2, y_gbp
    elif combo2.get() == "JPY": ybv, second_sel, yav = x_jpy, 3, y_jpy
    elif combo2.get() == "CNY": ybv, second_sel, yav = x_cny, 4, y_cny
    elif combo2.get() == "AZN": ybv, second_sel, yav = x_azn, 5, y_azn
    elif combo2.get() == "AUD": ybv, second_sel, yav = x_aud, 6, y_aud
    elif combo2.get() == "AMD": ybv, second_sel, yav = x_amd, 7, y_amd
    elif combo2.get() == "BYN": ybv, second_sel, yav = x_byn, 8, y_byn
    elif combo2.get() == "BGN": ybv, second_sel, yav = x_bgn, 9, y_bgn
    elif combo2.get() == "BRL": ybv, second_sel, yav = x_brl, 10, y_brl
    elif combo2.get() == "HUF": ybv, second_sel, yav = x_huf, 11, y_huf
    elif combo2.get() == "HKD": ybv, second_sel, yav = x_hkd, 12, y_hkd
    elif combo2.get() == "DKK": ybv, second_sel, yav = x_dkk, 13, y_dkk
    elif combo2.get() == "INR": ybv, second_sel, yav = x_inr, 14, y_inr
    elif combo2.get() == "CAD": ybv, second_sel, yav = x_cad, 15, y_cad
    elif combo2.get() == "KGS": ybv, second_sel, yav = x_kgs, 16, y_kgs
    elif combo2.get() == "NOK": ybv, second_sel, yav = x_nok, 17, y_nok
    elif combo2.get() == "PLN": ybv, second_sel, yav = x_pln, 18, y_pln
    elif combo2.get() == "RON": ybv, second_sel, yav = x_ron, 19, y_ron
    elif combo2.get() == "XDR": ybv, second_sel, yav = x_xdr, 20, y_xdr
    elif combo2.get() == "SGD": ybv, second_sel, yav = x_sgd, 21, y_sgd
    elif combo2.get() == "TJS": ybv, second_sel, yav = x_tjs, 22, y_tjs
    elif combo2.get() == "TRY": ybv, second_sel, yav = x_tryv, 23, y_tryv
    elif combo2.get() == "TMT": ybv, second_sel, yav = x_tmt, 24, y_tmt
    elif combo2.get() == "UZS": ybv, second_sel, yav = x_uzs, 25, y_uzs
    elif combo2.get() == "UAH": ybv, second_sel, yav = x_uah, 26, y_uah
    elif combo2.get() == "CZK": ybv, second_sel, yav = x_czk, 27, y_czk
    elif combo2.get() == "SEK": ybv, second_sel, yav = x_sek, 28, y_sek
    elif combo2.get() == "CHF": ybv, second_sel, yav = x_chf, 29, y_chf
    elif combo2.get() == "ZAR": ybv, second_sel, yav = x_zar, 30, y_zar
    elif combo2.get() == "KRW": ybv, second_sel, yav = x_krw, 31, y_krw
    messagebox.showinfo('Годовой курс', 'Годовой курс валюты '+ybv+' построен, см. Terminal и Figure 1')
    fy,fc=formatted_ya,formatted_current
    url2 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={0}&date_req2={1}&VAL_NM_RQ={2}'.format(fy,fc,yav)
    data2 = pd.read_xml(url2)
    val=data2["Value"]
    valo = list(val)
    valoa=str(valo).replace(", ","; ")
    valob=str(valoa).replace(",",".")
    valoc=str(valob).replace(";",",")
    hoh=str(valoc)
    gval = ast.literal_eval(hoh)
    gvaluta = list(map(float, gval))
    diapazon=data2["Date"]
    gdata = list(diapazon)
    js2 = second_sel
    svalse = js2
    data42={"svalse": svalse}
    with open('asl2.json', 'w') as f:
        json.dump(data42, f)
    x = gdata
    y = gvaluta
    fig = plt.figure(figsize=(15,5))
    plt.xticks(rotation=90, fontsize=5.1)
    titleone='Диапазон дат'
    titletwo='Значение курса валют'
    plt.xlabel(titleone, fontsize=11)
    plt.ylabel(titletwo, fontsize=11)
    plt.plot(x,y)
    plt.show()
def xv():
    global xav, xbv, date1, date2, third_sel
    if combo3.get() == "USD": xav, third_sel, xbv = y_usd, 0, x_usd
    elif combo3.get() == "EUR": xav, third_sel, xbv = y_eur, 1, x_eur
    elif combo3.get() == "GBP": xav, third_sel, xbv = y_gbp, 2, x_gbp
    elif combo3.get() == "JPY": xav, third_sel, xbv = y_jpy, 3, x_jpy
    elif combo3.get() == "CNY": xav, third_sel, xbv = y_cny, 4, x_cny
    elif combo3.get() == "AZN": xav, third_sel, xbv = y_azn, 5, x_azn
    elif combo3.get() == "AUD": xav, third_sel, xbv = y_aud, 6, x_aud
    elif combo3.get() == "AMD": xav, third_sel, xbv = y_amd, 7, x_amd
    elif combo3.get() == "BYN": xav, third_sel, xbv = y_byn, 8, x_byn
    elif combo3.get() == "BGN": xav, third_sel, xbv = y_bgn, 9, x_bgn
    elif combo3.get() == "BRL": xav, third_sel, xbv = y_brl, 10, x_brl
    elif combo3.get() == "HUF": xav, third_sel, xbv = y_huf, 11, x_huf
    elif combo3.get() == "HKD": xav, third_sel, xbv = y_hkd, 12, x_hkd
    elif combo3.get() == "DKK": xav, third_sel, xbv = y_dkk, 13, x_dkk
    elif combo3.get() == "INR": xav, third_sel, xbv = y_inr, 14, x_inr
    elif combo3.get() == "CAD": xav, third_sel, xbv = y_cad, 15, x_cad
    elif combo3.get() == "KGS": xav, third_sel, xbv = y_kgs, 16, x_kgs
    elif combo3.get() == "NOK": xav, third_sel, xbv = y_nok, 17, x_nok
    elif combo3.get() == "PLN": xav, third_sel, xbv = y_pln, 18, x_pln
    elif combo3.get() == "RON": xav, third_sel, xbv = y_ron, 19, x_ron
    elif combo3.get() == "XDR": xav, third_sel, xbv = y_xdr, 20, x_xdr
    elif combo3.get() == "SGD": xav, third_sel, xbv = y_sgd, 21, x_sgd
    elif combo3.get() == "TJS": xav, third_sel, xbv = y_tjs, 22, x_tjs
    elif combo3.get() == "TRY": xav, third_sel, xbv = y_tryv, 23, x_tryv
    elif combo3.get() == "TMT": xav, third_sel, xbv = y_tmt, 24, x_tmt
    elif combo3.get() == "UZS": xav, third_sel, xbv = y_uzs, 25, x_uzs
    elif combo3.get() == "UAH": xav, third_sel, xbv = y_uah, 26, x_uah
    elif combo3.get() == "CZK": xav, third_sel, xbv = y_czk, 27, x_czk
    elif combo3.get() == "SEK": xav, third_sel, xbv = y_sek, 28, x_sek
    elif combo3.get() == "CHF": xav, third_sel, xbv = y_chf, 29, x_chf
    elif combo3.get() == "ZAR": xav, third_sel, xbv = y_zar, 30, x_zar
    elif combo3.get() == "KRW": xav, third_sel, xbv = y_krw, 31, x_krw
    messagebox.showinfo('Курс валют для заданного диапазона','Курс валюты '+xbv+' построен'+'\n'+'см. Terminal и Figure 1')
    date1=en1.get()
    date2=en2.get()
    url3 = 'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={0}&date_req2={1}&VAL_NM_RQ={2}'.format(date1,date2,xav)
    data3 = pd.read_xml(url3)
    val=data3["Value"]
    valo = list(val)
    valoa=str(valo).replace(", ","; ")
    valob=str(valoa).replace(",",".")
    valoc=str(valob).replace(";",",")
    hoh=str(valoc)
    gval = ast.literal_eval(hoh)
    gvaluta = list(map(float, gval))
    diapazon=data3["Date"]
    gdata = list(diapazon)
    data4={"svalth": third_sel,"datefi": date1,"datese": date2}
    with open('dataforautosave.json', 'w') as f:
        json.dump(data4, f)
    with open('dataforautosave.json') as f:
        data4 = json.load(f)
    x = gdata
    y = gvaluta
    fig = plt.figure(figsize=(15,5))
    plt.xticks(rotation=90, fontsize=5.1)
    titleone='Диапазон дат'
    titletwo='Значение курса валют'
    plt.xlabel(titleone, fontsize=11)
    plt.ylabel(titletwo, fontsize=11)
    plt.plot(x,y)
    plt.show()
combo = Combobox(tab1, justify = "center", width = 5)
combo["values"] = ("USD","EUR","GBP","JPY","CNY","AZN","AUD","AMD","BYN","BGN","BRL","HUF","HKD","DKK","INR","CAD",
    "KGS","NOK","PLN","RON","XDR","SGD","TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW")
combo.current(svalfi)
combo.grid(column = 1, row = 0)
combo2 = Combobox(tab2, justify = "center", width = 5)
combo2["values"] = ("USD","EUR","GBP","JPY","CNY","AZN","AUD","AMD","BYN","BGN","BRL","HUF","HKD","DKK","INR","CAD",
    "KGS","NOK","PLN","RON","XDR","SGD","TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW")
combo2.current(svalse)
combo2.grid(column = 1, row = 10)
combo3 = Combobox(tab3, justify = "center", width = 5)
combo3["values"] = ("USD","EUR","GBP","JPY","CNY","AZN","AUD","AMD","BYN","BGN","BRL","HUF","HKD","DKK","INR","CAD",
    "KGS","NOK","PLN","RON","XDR","SGD","TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW")
combo3.current(svalth)
combo3.grid(column = 20, row = 25)
btn = Button(tab1, text = "Узнать курс ---> ",bg = '#8A2BE2',fg='#00FFFF',font='Consolas',command = av)
btn.grid(column = 3, row = 0)
label1=ttk.Label(tab1, text = "00.00000")
label1.grid(column = 4, row = 0)
label2=ttk.Label(tab3, text="Запишите в поля ввода две даты в формате ДД/ММ/ГГГГ:")
label2.grid(column = 0, row = 10, columnspan=2)
datelabel=ttk.Label(tab2, text = 'Сегодня: '+formatted_current+'\n'+'Сегодня, но год назад: '+formatted_ya)
datelabel.grid(column = 19, row = 7)
btn2 = Button(tab2, text = "Построить график за год",bg = '#8A2BE2',fg = '#00FFFF',font = 'Consolas',command = uv)
btn2.grid(row = 20, column = 20, pady = 20)
btn3 = Button(tab3,text = "Построить график за определённый диапазон",bg = '#8A2BE2',fg = '#00FFFF',font = 'Consolas',command = xv)
btn3.grid(row = 20, column = 20, pady = 20)
en1=Entry(tab3,width=32,fg = '#8A2BE2',bg = 'black',font = 'Consolas',insertbackground='#8A2BE2',textvariable = date1)
en1.grid(padx=1, pady=0)
en2=Entry(tab3,width=32,fg= '#8A2BE2',bg = 'black',font = 'Consolas',insertbackground='#8A2BE2',textvariable = date2)
en2.grid(padx=1, pady=5)
window.mainloop()