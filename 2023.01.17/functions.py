from data import *

def readFile(): 
    f = open("fob2016.txt", "r", encoding="UTF-8")
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    f.close()

def NoiVersenyzok():
    noiDb=0
    for item in versenyzok:
        if item.Kategoria == "Noi":
            noiDb+=1
    return noiDb/len(versenyzok)*100

def noiBajnok():
    bajnokPoz=0
    for i in range(len(versenyzok)):
        if versenyzok[i].Kategoria == "Noi" and versenyzok[i].osszpont() > versenyzok[bajnokPoz].osszpont:
            bajnokPoz = i
    return bajnokPoz

def ferfiPontok():
    f = open("osszpontFF.txt", "w", encoding="UTF-8")
    for item in versenyzok:
        if item.Kategoria == "Felnott ferfi":
            f.write(f"{item.Nev};{item.osszpont()}\n")
    f.close()

def stat():
    stat = {}
    for item in versenyzok:
        if item.Egyesulet != "n.a.":
            if item.Egyesulet in stat.keys():
                stat[item.Egyesulet] += 1
            else:
                stat[item.Egyesulet] = 1

    for key, value in stat.items():
        if value > 2:
            print(f"\t{key} - {value}") 