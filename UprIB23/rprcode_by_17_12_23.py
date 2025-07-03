import tkinter as tk
p, q, d, o, s = 7, 11, 67, [], []
n, x = p * q, (p - 1) * (q - 1)
def nod(a, b):
    while b != 0: a, b = b, a % b
    return a
def find_e(d, scorer1):
    for e in range(1, scorer1):
        if (e * d) % x == 1: o.append(e)
find_e(d, x)
print('Возможные значения открытого ключа от 1 до (p-1)*(q-1):', sorted(list(set(o))))
find_e(d, n)
print('Возможные значения открытого ключа от 1 до n:', sorted(list(set(o))))
def find_d(s, scorer2):
    for i in range(1, scorer2):
        if nod(i, x) == 1: s.append(i)
find_d(s, x)
print('Возможные значения закрытого ключа от 1 до (p-1)*(q-1):', sorted(list(set(s))))
find_d(s, n)
print('Возможные значения закрытого ключа от 1 до n:', sorted(list(set(s))))
def enc(text, e, x):
    e = 193
    while e < x:
        if (e * d) % x == 1: break
        else: e += 1
    enc_text = [pow((ord(char.lower()) - ord('а') + 1), e, n) for char in text]
    enc_text_str = " ".join(map(str, enc_text))
    return enc_text_str
def dec(enc_text, d, n):
    dec_text = ''.join([chr((pow(int(char), d, n) - 1) + ord('а')) for char in enc_text.split()])
    return dec_text
def enc_btn_click():
    text_getter = entry.get()
    enc_text = enc(text_getter, p, q)
    enc_lbl.config(text=f"Зашифрованный текст: {enc_text}")
    enc_lbl.pack()
def dec_btn_click():
    enc_text = entry.get()
    dec_text = dec(enc_text, d, n)
    dec_lbl.config(text=f"Расшифрованный текст: {dec_text}")
    dec_lbl.pack()
def copybtn(text):
    enc_text = enc(text, p, q)
    entry.delete(0, tk.END)
    entry.insert(0, enc_text)
def clearbtn(): entry.delete(0, tk.END)
win = tk.Tk()
win.geometry('700x300')
win.title("Шифрование/дешифрование по алгоритму Ривеста-Шамира-Адлемана (RSA)")
win.configure(bg='yellow')
label = tk.Label(win, text="Введите Ваш текст для шифрования/дешифрования:", bg='azure')
label.pack(pady=10)
entry = tk.Entry(win, width=57)
entry.config(bg='black', fg='yellow')
entry.pack()
enc_btn = tk.Button(win, text="Зашифровать", command=enc_btn_click, bg='purple', fg='yellow', width=50)
enc_btn.pack(pady=10)
copybutton = tk.Button(win, text="Ввести зашифрованный текст в поле ввода", command=lambda: copybtn(entry.get()),
                       bg='purple',fg='yellow', width=50)
copybutton.pack(pady=10)
dec_btn = tk.Button(win, text="Расшифровать", command=dec_btn_click, bg='purple', fg='yellow', width=50)
dec_btn.pack(pady=10)
clear_button = tk.Button(win, text="Очистить поле ввода", command=clearbtn, bg='purple', fg='yellow', width=50)
clear_button.pack(pady=10)
enc_lbl = tk.Label(win, bg='azure')
enc_lbl.config(text="Зашифрованный текст будет отображаться здесь...")
enc_lbl.pack()
dec_lbl = tk.Label(win, bg='azure')
dec_lbl.pack()
dec_lbl.config(text="Расшифрованный текст будет отображаться здесь...")
win.mainloop()