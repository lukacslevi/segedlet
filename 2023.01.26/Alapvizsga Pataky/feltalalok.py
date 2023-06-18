class feltalalo:
    def __init__(self, sor:str):
        adatok = sor.strip().split("/")
        self.nev = adatok[0]
        self.szulEv = int(adatok[1])
        if adatok[2] == "":
            self.halEv = 0
        else:
            self.halEv = int(adatok[2])
        self.talalmany = adatok[3]

feltalalok:list[feltalalo]=[]

f=open("feltalalok.txt", "r", encoding="UTF-8")
for sor in f:
    feltalalok.append(feltalalo(sor))
f.close()

print(f"2. feladat: a ")

print("3. feladat: feltalálók-találmányok")
for item in feltalalok:
    print(f"{item.nev} => {item.talalmanyok}")

kor = int(input("Kor megadása: "))
f = open("kiiras.txt", "w", encoding="Utf-8")
for item in feltalalok:
    if item.helEv-item.szulEv>kor:
        print(item.nev)
        f.write(f"{item.nev}\n")
f.close()

