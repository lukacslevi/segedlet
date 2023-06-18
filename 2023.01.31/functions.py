from data import *

def check(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def tokeletes(tol, ig):
    szamok = []
    for num in range(tol, ig):
        Sum = 0
        for i in range(1, num):
            if(num % i == 0):
                Sum = Sum + i
        if (Sum == num):
            szamok.append(num)
    return szamok

def readFile():
    f=open("ub2017egyeni.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        eredmenyek.append(eredmeny(sor))
    f.close()

def no():
    ossz = 0
    for item in eredmenyek:
        if item.kategoria == "Noi" and item.tavSzazalek == 100:
            ossz += 1
    return ossz