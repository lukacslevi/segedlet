from data import *

def readFile():
    file=open("hegyekMo.txt", "r", encoding="UTF-8")
    file.readline()
    for sor in file:
        hegyek.append(hegy(sor))
    file.close()

def atlag():
    all=0
    for item in hegyek:
        all += int(item.magassag)
    return str(all / len(hegyek)).replace(".", ",")

def highest():
    max = hegyek[0].magassag
    index = 0
    for i in range(1,len(hegyek)):
        if hegyek[i].magassag < max:
            max = hegyek[i].magassag
            index = i
    return index

def higher():
    limit = 3000 / 3.280839895
    num = 0
    for i in range(1, len(hegyek)):
        if int(hegyek[i].magassag) > limit:
            num += 1
    return num

def getMountains():
    mountains=[]
    for i in range(1, len(hegyek)):
        if hegyek[i].hegyseg in mountains:
            pass
        else: 
            mountains.append(hegyek[i].hegyseg)
    return mountains

def getHeights(list):
    for i in range(len(list)):
        osszeg=0
        for j in range(len(hegyek)):                #végigmegyünk a hegyeken, hegy=j
            if hegyek[j].hegyseg == list[i]:
                osszeg+=1
        print(f"\t{list[i]}: {osszeg} db")

def writeBukk():
    file=open("bukk-videk.txt", "w", encoding="UTF-8")
    file.write(f"Hegycsúcs neve;Hegység;Magasság\n")
    for i in hegyek:
        if i.hegyseg == "Bükk-vidék":
            file.write(f"{i.hegycsucs};{float(i.magassag)* 3.280839895 :.1f}\n")
    file.close()

