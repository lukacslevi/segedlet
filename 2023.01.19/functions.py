from data import *

def readFile():
    f=open("helsinki.txt", "r", encoding="UTF-8")
    for sor in f:
        eredmenyek.append(eredmeny(sor))
    f.close()

def helyezesekSzama(helyezes):
    db=0
    for item in eredmenyek:
        if item.helyezes == helyezes:
            db+=1
    return db

def osszpont():
    ossz=0
    for item in eredmenyek:
        ossz += item.pont()
    return ossz

def sportagErmek(sport):
    db=0
    for item in eredmenyek:
        if item.sportag == sport and item.helyezes <= 3:
            db+=1
    return db

def fajlbaIras():
    f=open("helsinki2.txt", "w", encoding="UTF-8")
    for item in eredmenyek:
        if item.sportag == "kajakkenu":
            f.write(f"{item.helyezes} {item.letszam} {item.pont()} kajak-kenu {item.versenyszam}\n")
        else:
            f.write(f"{item.helyezes} {item.letszam} {item.pont()} {item.sportag} {item.versenyszam}\n")
    f.close()

def maxLetszam():
    maxPoz=0
    for i in range(len(eredmenyek)):
        if eredmenyek[i].letszam > eredmenyek[maxPoz].letszam:
            maxPoz = i
    return maxPoz