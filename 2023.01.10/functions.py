from datetime import date
from data import *

def FajlBeolvas():
    fajl=open("fociVBk.csv", "r", encoding="UTF-8")
    fajl.readline()
    for sor in fajl:
        vbOrszagok.append(vbOrszag(sor))
    fajl.close()

def UtolsoVBnVolt():
    vb2018=[]
    for item in vbOrszagok:
        if item.Utolso==2018:
            vb2018.append(item.Orszag)
    for i in range(len(vb2018)):
        if i%4==0:
            print(f"{vb2018[i]:14}", end="")
        elif i%4==3:
            print(f"{vb2018[i]:14}")
        else:
            print(f"{vb2018[i]:14}", end="")

def BeNeLux():
    benelux=["Belgium", "Hollandia", "Luxemburg"]
    szereplesek=0
    for item in vbOrszagok:
        if item.Orszag in benelux:
            szereplesek+=item.Reszvetel
    return szereplesek

def ElsoVB():
    elso = vbOrszagok[0].Elso
    for item in vbOrszagok:
        if item.Elso < elso:
            elso = item.Elso
    return elso

def NyertesDb():
    db = 0
    for item in vbOrszagok:
        if "Világbajnok" in item.Eredmeny:
            db+=1
    return db

def Szlovakia():
    for item in vbOrszagok:
        if item.Orszag == "Szlovákia":
            return item.Eredmeny
    return "Szlovákia nem volt VB-n!"

def Kintvolte(orszag):
    for item in vbOrszagok:
        if item.Orszag == orszag and item.Elso == ElsoVB():
            return True
    return False

def Legtobbszor():
    f = open("legtobbszor.txt", "w", encoding="UTF-8")
    for item in vbOrszagok:
        if item.Reszvetel >= 10:
            f.write(f"{item.Orszag} {date.today().year-item.Elso}\n")
    f.close()