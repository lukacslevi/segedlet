from genericpath import exists
from data import tanulok
fajl='students.txt'  #a betöltendő fájl megadása /nem muszáj itt!!/

def menu():
    valasztott=''
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Új tanuló felvétele')
    print('2 - Tanulók kilistázása')
    print('3 - Tanulók mentése fájlba')
    print('4 - Tanulók betöltése fájlból (Új listába)')
    print('5 - Tanulók betöltése fájlból (Lista végére)')
    print('6 - Tanuló törlése')
    valasztott=input('Válasszon egy menüpontot: ')
    return valasztott


def fajlBetoltes():   #fájl tartalmának betöltése a listába
    if exists(fajl):
        file=open(fajl,'r',encoding='utf-8')
        for row in file:
            tanulok.append(row.strip())  #strip - eltávolítja a whitespace-eket a string elejéről és végéről
        file.close()
        input('A fájl betöltése sikeres volt.')

def tanulokKiirasa():
    print('Tanulók listája:')
    for i in range(0,len(tanulok)):
        print(f'\t{i+1}. {tanulok[i]}')

def ujTanulo():
    print('Új tanuló felvétele')
    nev=input('Kérem a tanuló nevét: ')
    tanulok.append(nev)
    input('A tanuló sikeresen felvételre került...')

def mentesFajlba():
    file=open('tanulok.txt','w',encoding='utf-8')
    for tanulo in tanulok:
        file.write(tanulo+'\n')  # \n - soremelés
    file.close()
    input('Sikeres mentés...')

def tanuloTorlese():
    tanulokKiirasa()
    torlendo=int(input('Kit szeretne törölni? Adja meg a sorszámát: '))
    #tanulok.remove(tanulok[torlendo-1])
    tanulok.pop(torlendo-1)
    input('A tanuló törlése sikeres...')


