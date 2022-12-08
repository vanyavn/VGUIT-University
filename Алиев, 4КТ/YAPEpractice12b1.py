def blokbex1():
    n = int(input("-->"))
    if n == 0:
        return 0
    else:
        return max(n, blokbex1())
print(blokbex1())  # Программа будет искать максимальное введённое значение n и не остановится, пока не будет введён нуль