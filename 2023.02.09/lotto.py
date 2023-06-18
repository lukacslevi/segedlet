

class sorsolas:
    def __init__(self,sor:str):
        adatok=sor.strip().split(" ")
        self.hetiSzamok=[]
        for szam in adatok:
            self.hetiSzamok.append(int(szam))

sorsolasok:list[sorsolas]=[]

bekert=sorsolas(input("1. feladat: Adja meg az 52. heti számokat: "))
print(f"\tNövekvő sorrendben: ",end="")
bekert.hetiSzamok.sort()
print(bekert.hetiSzamok)
for szam in bekert.hetiSzamok:
    print(f"{szam}", end="")

f=open("lottosz.txt","r",encoding="UTF-8")
for sor in f:
    sorsolasok.append(sorsolas(sor))
f.close()

szam = int(input("\n3. feladat: Kérem adja meg a hét számát (1-51): "))
print("\tNyerőszámok: ", end="")
for szam in sorsolasok[szam-1].hetiSzamok:
    print(f"{szam}", end="")
#print(f"\tNyerőszámok: {' '.join(str(e) for e in sorsolas[szam-1])}

eddigKihuzott = set()
for item in sorsolasok:
    for szam in item.hetiSzamok:
        eddigKihuzott.add(szam)
if len(eddigKihuzott)!=90:
    print(f"\nvan olyan szám amit nem húztak ki")
else:
    print(f"\nvan olyan szám amit nem húztak ki")

paratlanDb=0
for egyhet in sorsolasok:
    for szam in egyhet.hetiSzamok:
        if szam%2==1:
            paratlanDb+=1
print(paratlanDb + "alkalommal húztak páratlan számot")

sorsolasok.append(bekert)
f=open("lotto52.txt", "w", encoding="utf-8")
for egyhet in sorsolasok:
    f.write(f"{' '.join(str(e) for e in sorsolas[szam-1])}")