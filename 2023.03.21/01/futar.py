class Fuvar:
    def __init__(self, sor:str):
        data = sor.strip().split(" ")
        self.nap = int(data[0])
        self.fuvar = int(data[1])
        self.tav = int(data[2])

fuvarok:list[Fuvar] = []

f = open("tavok.txt", "r", encoding="UTF-8")
for sor in f:
    fuvarok.append(Fuvar(sor))
f.close()

min=0
nap=0
for i in range(len(fuvarok)):
    if fuvarok[i].nap <= fuvarok[min].nap:
        min = i
        nap = fuvarok[min].nap

for item in fuvarok:
    if item.nap == nap and item.fuvar == 1:
        print(f"2. feladat: Az első fuvar hossza: {item.tav} km")

max=0
maxnap=0
for i in range(len(fuvarok)):
    if fuvarok[i].nap > fuvarok[max].nap:
        max = i
        maxnap = fuvarok[max].nap

utolso = 0
utolsoTav=0
for item in fuvarok:
    if item.nap == maxnap:
        if item.fuvar > utolso:
            utolso = item.fuvar
            utolsoTav = item.tav

print(f"3. feladat: Az utolsó fuvar hossza: {utolsoTav} km")
het = [1, 2, 3, 4, 5, 6, 7]
for item in fuvarok:
    if item.nap in het:
        het.remove(item.nap)

print("4. feladat: A futár az alapábbi napokon nem dolgozott:")
for item in het:
    print(f"\t{item}. nap")

max=0
for i in range(len(fuvarok)):
    if fuvarok[i].tav > fuvarok[max].tav:
        max = i
print(f"5. feladat: A legtöbb fuvar a hét {fuvarok[max].nap}. napján volt, összesen {fuvarok[max].tav} db")

stat = {}
for item in fuvarok:
    if item.nap in stat.keys():
        stat[item.nap] += item.tav
    else: 
        stat[item.nap] = item.tav

print("6. feladat: Az egyes napokon tekert km-ek:")
for key, value in stat.items():
    print(f"\t{key}.nap : {value} km")

def DijSzamol(tav):
    if tav >= 1 and tav <= 2:
        return 500
    if tav >= 3 and tav <= 5:
        return 700
    if tav >= 6 and tav <= 10:
        return 900
    if tav >= 11 and tav <= 20:
        return 1400
    if tav >= 21 and tav <= 30:
        return 2000
    
input = int(input("Adjon meg egy távolságot: "))
print(DijSzamol(input))

f = open("dijazas.txt", "w", encoding="UTF-8")
for item in fuvarok:
    f.write(f"{item.nap}.nap {item.fuvar} út. {DijSzamol(item.tav)} Ft\n")
f.close()

sum = 0
for item in fuvarok:
    sum += DijSzamol(item.tav)
print(sum)
