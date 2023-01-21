from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox, scrolledtext, ttk, Tk
from tkinter.ttk import Combobox
import requests
uvu = 'Курс'
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
usd = data['Valute']['USD']['Value']
x_usd = data['Valute']['USD']['Name']
eur = data['Valute']['EUR']['Value']
x_eur = data['Valute']['EUR']['Name']
gbp = data['Valute']['GBP']['Value']
x_gbp = data['Valute']['GBP']['Name']
jpy = data['Valute']['JPY']['Value']
x_jpy = data['Valute']['JPY']['Name']
cny = data['Valute']['CNY']['Value']
x_cny = data['Valute']['CNY']['Name']
azn = data['Valute']['AZN']['Value']
x_azn = data['Valute']['AZN']['Name']
aud = data['Valute']['AUD']['Value']
x_aud = data['Valute']['AUD']['Name']
amd = data['Valute']['AMD']['Value']
x_amd = data['Valute']['AMD']['Name']
byn = data['Valute']['BYN']['Value']
x_byn = data['Valute']['BYN']['Name']
bgn = data['Valute']['BGN']['Value']
x_bgn = data['Valute']['BGN']['Name']
brl = data['Valute']['BRL']['Value']
x_brl = data['Valute']['BRL']['Name']
huf = data['Valute']['HUF']['Value']
x_huf = data['Valute']['HUF']['Name']
hkd = data['Valute']['HKD']['Value']
x_hkd = data['Valute']['HKD']['Name']
dkk = data['Valute']['DKK']['Value']
x_dkk = data['Valute']['DKK']['Name']
inr = data['Valute']['INR']['Value']
x_inr = data['Valute']['INR']['Name']
cad = data['Valute']['CAD']['Value']
x_cad = data['Valute']['CAD']['Name']
kgs = data['Valute']['KGS']['Value']
x_kgs = data['Valute']['KGS']['Name']
nok = data['Valute']['NOK']['Value']
x_nok = data['Valute']['NOK']['Name']
pln = data['Valute']['PLN']['Value']
x_pln = data['Valute']['PLN']['Name']
ron = data['Valute']['RON']['Value']
x_ron = data['Valute']['RON']['Name']
xdr = data['Valute']['XDR']['Value']
x_xdr = data['Valute']['XDR']['Name']
sgd = data['Valute']['SGD']['Value']
x_sgd = data['Valute']['SGD']['Name']
tjs = data['Valute']['TJS']['Value']
x_tjs = data['Valute']['TJS']['Name']
tryv = data['Valute']['TRY']['Value']
x_tryv = data['Valute']['TRY']['Name']
tmt = data['Valute']['TMT']['Value']
x_tmt = data['Valute']['TMT']['Name']
uzs = data['Valute']['UZS']['Value']
x_uzs = data['Valute']['UZS']['Name']
uah = data['Valute']['UAH']['Value']
x_uah = data['Valute']['UAH']['Name']
czk = data['Valute']['CZK']['Value']
x_czk = data['Valute']['CZK']['Name']
sek = data['Valute']['SEK']['Value']
x_sek = data['Valute']['SEK']['Name']
chf = data['Valute']['CHF']['Value']
x_chf = data['Valute']['CHF']['Name']
zar = data['Valute']['ZAR']['Value']
x_zar = data['Valute']['ZAR']['Name']
krw = data['Valute']['KRW']['Value']
x_krw = data['Valute']['KRW']['Name']
window = Tk()
window.title("Январьская практика, ИЗ№3, демо")
window.geometry("700x500")
window['bg'] = '#8A2BE2'
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Курс валют")
def clik():
    if combo.get() == "AZN": label1.configure(text=str(azn)+' рублей'+'\n'+x_azn)
    elif combo.get() == "AUD": label1.configure(text=str(aud)+' рублей'+'\n'+x_aud)
    elif combo.get() == "AMD": label1.configure(text=str(amd)+' рублей'+'\n'+x_amd)
    elif combo.get() == "BYN": label1.configure(text=str(byn)+' рублей'+'\n'+x_byn)
    elif combo.get() == "BGN": label1.configure(text=str(bgn)+' рублей'+'\n'+x_bgn)
    elif combo.get() == "BRL": label1.configure(text=str(brl)+' рублей'+'\n'+x_brl)
    elif combo.get() == "HUF": label1.configure(text=str(huf)+' рублей'+'\n'+x_huf)
    elif combo.get() == "HKD": label1.configure(text=str(hkd)+' рублей'+'\n'+x_hkd)
    elif combo.get() == "DKK": label1.configure(text=str(dkk)+' рублей'+'\n'+x_dkk)
    elif combo.get() == "INR": label1.configure(text=str(inr)+' рублей'+'\n'+x_inr)
    elif combo.get() == "CAD": label1.configure(text=str(cad)+' рублей'+'\n'+x_cad)
    elif combo.get() == "KGS": label1.configure(text=str(kgs)+' рублей'+'\n'+x_kgs)
    elif combo.get() == "NOK": label1.configure(text=str(nok)+' рублей'+'\n'+x_nok)
    elif combo.get() == "PLN": label1.configure(text=str(pln)+' рублей'+'\n'+x_pln)
    elif combo.get() == "RON": label1.configure(text=str(ron)+' рублей'+'\n'+x_ron)
    elif combo.get() == "XDR": label1.configure(text=str(xdr)+' рублей'+'\n'+x_xdr)
    elif combo.get() == "SGD": label1.configure(text=str(sgd)+' рублей'+'\n'+x_sgd)
    elif combo.get() == "TJS": label1.configure(text=str(tjs)+' рублей'+'\n'+x_tjs)
    elif combo.get() == "TRY": label1.configure(text=str(tryv)+' рублей'+'\n'+x_tryv)
    elif combo.get() == "TMT": label1.configure(text=str(tmt)+' рублей'+'\n'+x_tmt)
    elif combo.get() == "UZS": label1.configure(text=str(uzs)+' рублей'+'\n'+x_uzs)
    elif combo.get() == "UAH": label1.configure(text=str(uah)+' рублей'+'\n'+x_uah)
    elif combo.get() == "CZK": label1.configure(text=str(czk)+' рублей'+'\n'+x_czk)
    elif combo.get() == "SEK": label1.configure(text=str(sek)+' рублей'+'\n'+x_sek)
    elif combo.get() == "CHF": label1.configure(text=str(chf)+' рублей'+'\n'+x_chf)
    elif combo.get() == "ZAR": label1.configure(text=str(zar)+' рублей'+'\n'+x_zar)
    elif combo.get() == "KRW": label1.configure(text=str(krw)+' рублей'+'\n'+x_krw)
tab_control.add(tab3, text = "*")
tab_control.pack(expand = 1, fill = 'both')
def clik2():
    with open('godsavethekurs.txt','r') as file:
        text.insert(1.0, file.read())
    file.close()
def clik3():
    with open('godsavethekurs.txt','w') as file1:
         file1.write(text.get(1.0, END))
    file1.close()
var = IntVar()
var.set(0)
combo = Combobox(tab1, justify = "center", width = 5)
combo["values"] = ("AZN", "AUD", "AMD", "BYN", "BGN", "BRL", "HUF", "HKD", "DKK", "INR", "CAD", "KGS", "NOK",
    "PLN", "RON", "XDR", "SGD", "TJS", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "ZAR", "KRW")
combo.current(5)
combo.grid(column = 1, row = 0)
var1 = IntVar()
var1.set(0)
btn = Button(tab1, text = "Узнать курс ---> ", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik)
btn.grid(column = 3, row = 0)
label1 = ttk.Label(tab1, text = "0")
label1.grid(column = 4, row = 0)
label2 = ttk.Label(tab1, text = "Другие валюты: "+"\nПопулярные валюты: ")
label2.grid(column = 0, row = 0)
label3 = ttk.Label(tab3, text = "ЧЁ СМОТРИШЬ?")
label3.grid(column = 5, row = 5)
label4 = ttk.Label(tab1, text = "График: "+"\nЭто демка, увы :(")
label4.grid(column = 0, row = 9)
label5 = ttk.Label(tab1, text = " <--- Ваш отзыв")
label5.grid(column = 7, row = 7)
selected = BooleanVar()
selected.set(0)
chs1 = BooleanVar()
chs2 = BooleanVar()
chs3 = BooleanVar()
chs4 = BooleanVar()
chs5 = BooleanVar()
chs1.set(True)
chs2.set(True)
chs3.set(True)
chs4.set(True)
chs5.set(True)
selected = IntVar()
def clik1():
   if chk_state.get()==True:
        label1.configure(text=str(usd)+' рублей'+'\n'+x_usd)
        messagebox.showinfo('Курс доллара', str(usd)+' рублей')
   if chk_state2.get()==True:
        label1.configure(text=str(eur)+' рублей'+'\n'+x_eur)
        messagebox.showinfo('Курс евро', str(eur)+' рублей')
   if chk_state3.get()==True:
        label1.configure(text=str(gbp)+' рублей'+'\n'+x_gbp)
        messagebox.showinfo('Курс фунта стерлингов', str(gbp)+' рублей')
   if chk_state4.get()==True:
        label1.configure(text=str(jpy)+' рублей'+'\n'+x_jpy)
        messagebox.showinfo('Курс японской йены', str(jpy)+' рублей')
   if chk_state5.get()==True:
        label1.configure(text=str(cny)+' рублей'+'\n'+x_cny)
        messagebox.showinfo('Курс китайской юани', str(cny)+' рублей')
chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(tab1, text='$', var=chk_state)
chk.grid(column = 0, row = 4)
chk_state2 = BooleanVar()
chk_state2.set(False)
chk2 = Checkbutton(tab1, text='€', var=chk_state2)
chk2.grid(column = 1, row = 4)
chk_state3 = BooleanVar()
chk_state3.set(False)
chk3 = Checkbutton(tab1, text='£', var=chk_state3)
chk3.grid(column = 2, row = 4)
chk_state4 = BooleanVar()
chk_state4.set(False)
chk4 = Checkbutton(tab1, text='¥ (яп.)', var=chk_state4)
chk4.grid(column = 3, row = 4)
chk_state5 = BooleanVar()
chk_state5.set(False)
chk5 = Checkbutton(tab1, text='¥ (кит.)', var=chk_state5)
chk5.grid(column=4, row=4)
btn1 = Button(tab1, text = "Нажмите кнопку!", bg = '#8A2BE2', fg='#00FFFF', font = 'Consolas', command = clik1)
btn1.grid(column = 0, row = 5)
text = scrolledtext.ScrolledText(tab1, width = 25, height = 1, bg='#8A2BE2', fg = '#00FFFF', font = 'Consolas')
text.grid(row = 7, column = 1, columnspan=9000, padx=8)
btn2 = Button(tab1, text = "Загузить", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik2)
btn2.grid(row = 7, column = 0, pady = 10)
btn3 = Button(tab1, text = "Сохранить", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik3)
btn3.grid(row = 7, column = 1)
window.mainloop()