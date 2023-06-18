from math import sqrt

print("1. feladat: Háromszög kerülete és területe\nKérem a háromszög oldalait")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

k = a+b+c
print(f"K = {k}")
s= k / 2
t = sqrt(s*(s-a)*(s-b)*(s-c))
print(f"T = {t}")