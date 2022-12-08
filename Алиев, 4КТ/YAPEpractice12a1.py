def fac(n): # x^n/n!
    if n == 0:
        return 1
    else:
        return fac(n-1) * n
def ddf(x, n):
    w = x**n/fac(n)
    print(w)
a = int(input('x-->'))
b = int(input('n-->'))
fac(a)
ddf(a, b)