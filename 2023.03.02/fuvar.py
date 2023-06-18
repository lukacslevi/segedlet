import datetime

class Fuvar:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.azonosito = int(adatok[0])
        self.indulas = datetime.strptime(adatok[1], "%Y-%m-%d %H:%M:%S")
        self.idotartam = int(adatok[2])
        self.tavolsag = float(adatok[3].replace(",", "."))
        self.viteldij = float(adatok[4].replace(",", "."))
        self.borravalo = float(adatok[5].replace(",", "."))
        self.fizetes = adatok[6]

fuvarok:list[Fuvar] = []

f=open("fuvar.csv", "r", encoding="UTF-8")
elsoSor = f.readline().strip()
for sor in f:
    fuvarok.append(Fuvar(sor))
f.close()

print(f"3. feladat: {len(fuvarok)} fuvar")

fuvarDb = 0
penz = 0
for fuvar in fuvarok:
    if fuvar.azonosito == 6185:
        fuvarDb+=1
        penz+=fuvar.viteldij
print(f"{fuvarDb} fuvar alatt: {penz}$")

fizetesiMod={}
for fuvar in fuvarok:
    if fuvar.fizetes in fizetesiMod.keys():
        fizetesiMod[fuvar.fizetes]+=1
    else:
        fizetesiMod[fuvar.fizetes]=1

print("5. feladat:")
for key, value in fizetesiMod.items():
    print(f"{key}: {value} fuvar")

osszTav=0
for fuvar in fuvarok:
    osszTav+=fuvar.tavolsag
print(f"6.feladat: {osszTav}km")

maxIdoPoz=0
for i in range(len(fuvarok)):
    if fuvarok[i].idotartam > fuvarok[maxIdoPoz].idotartam:
        maxIdoPoz = i

print("7. feladat: ")




ellFuvar=sorted(fuvarok, key=lambda x: x.indulas, reverse=False)