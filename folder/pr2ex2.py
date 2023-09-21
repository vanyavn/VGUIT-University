n = int(input("N = "))
m = int(input("M = "))
c = 0
while n >= 0:
    c += 1
    n -= m * c
x = 'Вода перельётся через {0} заходов'.format(c)
print(x)