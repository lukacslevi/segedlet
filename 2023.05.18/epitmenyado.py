class Epitmeny:
    def __init__(self, line:str):
        data = line.strip().split(" ")
        self.owner = data[0]
        self.street = data[1]
        self.num = data[2]
        self.zone = data[3]
        self.area = int(data[4])

epitmenyek:list[Epitmeny] = []

f = open("utca.txt", "r", encoding="utf-8")
zoneprices = f.readline().strip().split(" ")
for line in f:
    epitmenyek.append(Epitmeny(line))
f.close()

#2
print(f"2. feladat. A mintában {len(epitmenyek)} telek szerepel.")

#3
search = input(f"3. feladat. Egy tulajdonos adószáma = ")
for item in epitmenyek:
    if item.owner == search:
        print(f"{item.street} utca {item.num}")

#4
def ado(zone, area):
    ado=0
    if zone == "A":
        ado = area * int(zoneprices[0])
    elif zone == "B":
        ado = area * int(zoneprices[1])
    else:
        ado = area * int(zoneprices [2])
    if ado >= 10000:
        return ado
    else: 
        return 0
    
#5
print(f"5. feladat", end="")
zones = ["A", "B", "C"]
for zone in zones:
    num = 0
    areas= 0
    for item in epitmenyek:
        if item.zone == zone:
            num+=1
            areas += item.area
    print(f"{zone} sávba {num} telek esik, az adó {ado(zone, areas)} Ft")
            

