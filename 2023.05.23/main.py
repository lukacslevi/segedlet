class Repulo:
    def __init__(self, sor:str):
        data=sor.strip().split(";")
        self.tipus = data[0]
        self.ev = int(data[1])
        self.utas=data[2]
        self.szemelyzet=data[3]
        self.sebesseg=int(data[4])
        self.tomeg=int(data[5])
        self.fesztav=float(data[6].replace(",", "."))
        self.sebessegKat=""
        if (self.sebesseg < 500):
            self.sebessegKat="Alacsony sebességű"
        elif (self.sebesseg < 1000):
            self.sebessegKat="Szubszonikus"
        elif (self.sebesseg < 1200):
            self.sebessegKat = "Transzszonikus"
        else:
            self.sebessegKat = "Szuperszonikus"

repulok:list[Repulo] = []

f=open("utasszallitok.txt", "r", encoding="utf-8")
f.readline()
for line in f:
    repulok.append(Repulo(line))
f.close()

print(f"4. feladat: Adatsorok száma: {len(repulok)}")
boeingDb=0
for repulo in repulok:
    if repulo.tipus.__contains__("Boeing"):
        boeingDb+=1
print(f"5. feladat: Boein típusok száma: {boeingDb}")

maxUtasPoz = 0
maxUtas = 0
for i in range(len(repulok)):
    utasszam=int(repulok[i].utas.split("-")[-1])
    if utasszam > maxUtas:
        maxUtas = utasszam
        maxUtasPoz = i

print(f"\tTípus{repulok[maxUtasPoz].tipus}")

stat = {
    "Alacsony sebességű":0,
    "Szubszonikus": 0,
    "Transzszonikus": 0,
    "Szuperszonikus": 0
}

for repulo in repulok:
    if repulo.sebessegKat in stat.keys():
        stat[repulo.sebessegKat] +=1
db=0
for key, value in stat.items():
    if value==0:
        print(f"\t{key}", end=" ")
        db+=1

