import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
def show_dataframe(df):
    df_window = tk.Toplevel(root)
    df_window.title("Шифрование")
    df_window.geometry("250x200") # iat - доступ к элементу i строки j столбца
    for i in range(len(df.index)):
        for j in range(len(df.columns)): 
            cell = tk.Label(df_window, text=df.iat[i, j] if pd.notna(df.iat[i, j]) else "", borderwidth=1,
                            relief="solid", width=5, height=2)
            cell.grid(row=i, column=j, padx=2, pady=2)
def copy_to_input(encrypted_message):
    entry.delete(0, tk.END)
    entry.insert(0, encrypted_message)
def encrypt():
    name = entry.get()  # Получаем введенное имя из поля ввода
    if len(name) > 20:
        messagebox.showerror("Ошибка", "Имя должно быть не длиннее 20 символов.")
        return
    # Подгоняем длину имени под 20 символов, заполняя недостающие символы пробелами
    name = name.ljust(20)
    symb_list = list(name)
    # Объявление DataFrame размером 5x4, заполненного значениями NaN
    data = pd.DataFrame({"1": [np.nan] * 5,
                         "2": [np.nan] * 5,
                         "3": [np.nan] * 5,
                         "4": [np.nan] * 5},
                        index=["1", "2", "3", "4", "5"])

    indx = 0
    for row in ["1", "2", "3", "4", "5"]:
        for col in ["1", "2", "3", "4"]:
            if indx >= len(symb_list):
                break
            data.at[row, col] = symb_list[indx]
            indx += 1
    # Перестановка столбцов по ключу k2
    key2 = [4, 3, 2, 1]
    encrypted_columns = [list(data[str(col)]) for col in key2]
    encrypted_message = ""
    for column in encrypted_columns:
        for character in column:
            if isinstance(character, str):
                encrypted_message += character
    messagebox.showinfo("Зашифрованное сообщение", encrypted_message)
    show_df_button = tk.Button(root, text="Показать датафрейм", bg = "purple", command=lambda: show_dataframe(data))
    show_df_button.pack(pady=5)
    copy_input_button = tk.Button(root, text="Копировать зашифрованную строку в поле ввода", bg = "purple",
                                  command=lambda: copy_to_input(encrypted_message))
    copy_input_button.pack(pady=5)
def decrypt():
    name = entry.get()  # Получаем введенное имя из поля ввода
    if len(name) > 20:
        messagebox.showerror("Ошибка", "Имя должно быть не длиннее 20 символов.")
        return
    # Подгоняем длину имени под 20 символов, заполняя недостающие символы пробелами
    name = name.ljust(20)
    symb_list = list(name)
    # Объявление DataFrame размером 5x4, заполненного значениями NaN
    data = pd.DataFrame({"1": [np.nan] * 5,
                         "2": [np.nan] * 5,
                         "3": [np.nan] * 5,
                         "4": [np.nan] * 5},
                        index=["1", "2", "3", "4", "5"])
    indx = 0
    for row in ["1", "2", "3", "4", "5"]:
        for col in ["1", "2", "3", "4"]:
            if indx >= len(symb_list):
                break
            data.at[row, col] = symb_list[indx]
            indx += 1
    # Извлечение символов из DataFrame в исходном порядке
    decryption_sequence = [data["1"]["1"], data["2"]["1"], data["3"]["1"], data["4"]["1"],
                           data["1"]["2"], data["2"]["2"], data["3"]["2"], data["4"]["2"],
                           data["1"]["3"], data["2"]["3"], data["3"]["3"], data["4"]["3"],
                           data["1"]["4"], data["2"]["4"], data["3"]["4"], data["4"]["4"],
                           data["1"]["5"], data["2"]["5"], data["3"]["5"], data["4"]["5"]]
    decrypted_message = ""
    for symbol in decryption_sequence:
        if isinstance(symbol, str):
            decrypted_message += symbol
    messagebox.showinfo("Расшифрованное сообщение", decrypted_message)
root = tk.Tk()
root.title("Шифрование перестановкой")
root.geometry("500x300")
label = tk.Label(root, text="Введите Ваше имя:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)
encrypt_button = tk.Button(root, text="Зашифровать", command=encrypt, bg = "red")
encrypt_button.pack(pady=5)
decrypt_button = tk.Button(root, text="Расшифровать", command=decrypt, bg = "blue")
decrypt_button.pack(pady=5)
root.mainloop()