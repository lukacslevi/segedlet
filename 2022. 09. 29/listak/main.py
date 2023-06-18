from random import randint

szamok = []

def listaFeltolt(elemszam, alsoKuszob=0, felsoKuszob=100):
    for i in range(0, elemszam):
        szamok.append(randint(alsoKuszob, felsoKuszob))

def listaSorszamozottKiir():
    index=1
    for egySzam in szamok:
        print(f'{index}.: {egySzam}')
        index+=1

def listaSorszamozottKiir2():
    for i in range(0, len(szamok)):
        print(f'{i+1}.: {szamok[i]}')

def listaSorszamozottKiir3():
    for index, szam in enumerate(szamok):
        print(f'{index+1}.: {szam}')
        

listaFeltolt(20,20,40)
listaSorszamozottKiir2()

szamok.remove(szamok[0]) 
szamok.pop(0)
listaSorszamozottKiir3()