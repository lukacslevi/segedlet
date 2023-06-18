from data import nevek, ugrasok
from os import system
fajlnev='jumps.csv'

def menu():
    system('cls')
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Versenyzők')
    print('2 - Eredmények')
    print('3 - Új eredmény felvétele')
    print('4 - Eredmények törlése')
    return input('Választás: ')

def fajlBetoltes():
    file=open(fajlnev,'r',encoding='utf-8')
    for row in file:
        #row -> Kovács Béla;7.56\n
        darabolt=row.strip().split(';')
        #print(darabolt)
        nevek.append(darabolt[0])
        ugrasok.append(float(darabolt[1]))
    file.close()

def versenyzoKiir():
    system("cls")
    print("------------- VERSENYZŐK -------------")
    for nev in nevek:
        print(f"\t{nev}")
    input()

def eredmenyKiir():
    system("cls")
    print("------------- EREDMÉNYEK -------------")
    for i in range(1, len(nevek)):
        print(f"\t{i+1}. {nevek[i]}: {ugrasok[i]} m")
    
def ujEredmeny():
    system("cls")
    print("------------- ÚJ EREDMÉNY -------------")
    bekertNev=input("Név: ")
    bekertUgras=float(input("Ugrás: "))
    nevek.append(bekertNev)
    ugrasok.append(bekertUgras)
    eredmenyMenteseFajlVegere(bekertNev, bekertUgras)
    input("Sikeres mentés!")

def eredmenyMenteseFajlVegere(nev, ugras):
    file=open(fajlnev, "a", encoding="utf-8")
    file.write(f"{nev};{ugras}")
    file.close()

def eredmenyTorlese():
    system("cls")
    print("------------ EREDMÉNY TÖRLÉSE ---------")
    eredmenyKiir()
    sSz=int(input("\nKit töröljünk?"))
    nevek.pop(sSz-1)
    ugrasok.pop(sSz-1)
    input("Sikeres törlés!")

def mentesFajlba():
    file=open(fajlnev,"w",encoding="utf-8")
    for i in range(len(nevek)):
        if i>0:
            file.write("\n")
        file.write(f"\n{nevek[i]};{ugrasok[i]}")
    file.close