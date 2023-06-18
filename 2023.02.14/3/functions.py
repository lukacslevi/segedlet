from data import *

def readFile():
    f=open("nevek.txt", "r", encoding="UTF-8")
    for sor in f:
        tanulok.append(tanulo(sor))
    f.close()

def countName(name):
    length = 0
    for letter in name:
        if letter != " ":
            length+=1
    return int(length)

def username(ev, osztaly, nev):
    elso = str(ev)[len(str(ev)) - 1]
    masodik = osztaly
    nevDarabolt = nev.split(" ")
    harmadik = (nevDarabolt[0])[0:3].lower()
    negyedik = (nevDarabolt[1])[0:3].lower()
    return elso + masodik + harmadik + negyedik