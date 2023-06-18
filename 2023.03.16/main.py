class Sakkozo:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.azonosito = adatok[0]
        self.nev = adatok[1]
        self.orszag = adatok[2]
        self.nem = adatok[3]
        self.psz = int(adatok[4])
        self.szul = adatok[5]
    
    def szupernm(self):
        if self.nem == "N" and self.psz >= 2500:
            return True
            
        elif self.nem == "F" and self.psz >= 2700:
            return True
        else:
            return False

sakkozok:list[Sakkozo] = []

def readFile():
    f = open("sakk.txt", "r", encoding="UTF-8")
    f.readline()
    for sor in f:
        sakkozok.append(Sakkozo(sor))
    f.close()

readFile()
#4.
print(f"4. feladat: Versenyzők száma: {len(sakkozok)}")

#5.
nok=0
for item in sakkozok:
    if item.nem == "N":
        nok +=1

print(f"5. feladat: Női versenyzők aránya: {nok/len(sakkozok)*100}%")

#6.


#7.
sznm=0
for item in sakkozok:
    if Sakkozo.szupernm(item):
        sznm +=1
print(f"7. feladat: Szupernagymesterk száma: {sznm} fő")

#8.
f_psz=0
n_psz=0
ferfi=0
noi=0
for i in range(len(sakkozok)):
    if sakkozok[i].nem == "F":
        if sakkozok[i].psz > f_psz:
            f_psz = sakkozok[i].psz
            ferfi = i
    if sakkozok[i].nem == "N":
        if sakkozok[i].psz > n_psz:
            n_psz = sakkozok[i].psz
            noi = i

print("8. feladat: A ranglistát vezető sakkozók:")
print(f"\tFérfi: {sakkozok[ferfi].nev}({sakkozok[ferfi].orszag}) - azonosító: {sakkozok[ferfi].azonosito} - {f_psz}")
print(f"\tNői: {sakkozok[noi].nev}({sakkozok[noi].orszag}) - azonosító: {sakkozok[noi].azonosito} - {n_psz}")

#9.
print("9. feladat:")
ev = input(f"\tÉv:")
for item in sakkozok:
    if item.szul == ev:
        print(f'\tAz adott évben született versenyző')
        break
else:
    print(f'\tnope')
