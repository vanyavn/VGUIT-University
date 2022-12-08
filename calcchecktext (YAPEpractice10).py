from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter import messagebox, scrolledtext, ttk, Tk
from tkinter.ttk import Combobox

uvu = 'Ваш выбор'
errortext = 'Ошибка'
frst = 'Первый'
scnd = 'Второй'
thrd = 'Третий'
frstw = 'Вы выбрали первый'
scndw = 'Вы выбрали второй'
thrdw = 'Вы выбрали третий'

window = Tk()
window.title("Алиев Иван, УБ-21")
window.geometry("572x572")
window['bg'] = '#8A2BE2'

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text = "Калькулятор")
def clik():
    if combo.get() == "+": label1.configure(text=int(spin.get()) + int(spin1.get()))
    elif combo.get() == "-": label1.configure(text=int(spin.get()) - int(spin1.get()))
    elif combo.get() == "*": label1.configure(text=int(spin.get()) * int(spin1.get()))
    elif combo.get() == "/" and spin1.get() == "0":
        messagebox.showinfo(errortext, "На ноль делить нельзя")
    else:
        label1.configure(text=int(spin.get()) / int(spin1.get()))
tab_control.add(tab2, text = "Три чекбокса")
tab_control.add(tab3, text = "Работа с текстом")
tab_control.pack(expand = 1, fill = 'both')

def clik2():
    with open('text.txt','r') as file:
        text.insert(1.0, file.read())
    file.close()
def clik3():
    with open('text.txt','w') as file1:
         file1.write(text.get(1.0, END))
    file1.close()

var = IntVar()
var.set(0)
spin = Spinbox(tab1,from_ = -100000, to = 100000, width = 10, bg='#8A2BE2', fg='#00FFFF', font = 'Consolas',
justify = "center", textvariable = var)
spin.grid(column = 0, row = 0)

combo = Combobox(tab1, justify = "center", width = 5)
combo["values"] = ("+", "-", "*", "/")
combo.current(0)
combo.grid(column = 1, row = 0)

var1 = IntVar()
var1.set(0)

spin1 = Spinbox(tab1, from_ = -100000, to = 100000, width =10, bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas',
justify = "center", textvariable = var1)
spin1.grid(column = 2, row = 0)
btn = Button(tab1, text = "=", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik)
btn.grid(column = 3, row = 0)

label1 = ttk.Label(tab1, text = "0")
label1.grid(column = 4, row = 0)

selected = BooleanVar()
selected.set(0)

chs1 = BooleanVar()
chs2 = BooleanVar()
chs3 = BooleanVar()
chs1.set(True)
chs2.set(True)
chs3.set(True)

selected = IntVar()

def clik1():
   if chk_state.get()==True: messagebox.showinfo(uvu,frstw)
   if chk_state2.get()==True: messagebox.showinfo(uvu,scndw)
   if chk_state3.get()==True: messagebox.showinfo(uvu,thrdw)

chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(tab2, text=frst, var=chk_state)
chk.grid(column=0, row=0)
chk_state2 = BooleanVar()
chk_state2.set(False)
chk2 = Checkbutton(tab2, text=scnd, var=chk_state2)
chk2.grid(column=1, row=0)
chk_state3 = BooleanVar()
chk_state3.set(False)
chk3 = Checkbutton(tab2, text=thrd, var=chk_state3)
chk3.grid(column=2, row=0)

btn1 = Button(tab2, text = "Нажмите кнопку!", bg = '#8A2BE2', fg='#00FFFF', font = 'Consolas', command = clik1)
btn1.grid(column = 0, row = 5)
text = scrolledtext.ScrolledText(tab3, width = 43, height=10, bg='#8A2BE2', fg = '#00FFFF', font = 'Consolas')
text.grid(row = 0, column = 0, columnspan=2, padx=35)

btn2 = Button(tab3, text = "Загузить", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik2)
btn2.grid(row = 1, column = 0, pady = 10)

btn3 = Button(tab3, text = "Сохранить", bg = '#8A2BE2', fg = '#00FFFF', font = 'Consolas', command = clik3)
btn3.grid(row = 1, column = 1)

window.mainloop()