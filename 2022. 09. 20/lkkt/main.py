#lkkt

def lkkt(a,b):
    if a>b:
        nsz=a
        ksz=b
    else:
        nsz=b
        ksz=a
    osztando=nsz
    while osztando % ksz!= 0:
        osztando +=nsz
    return osztando
print("Lekisebb közös többszörös meghatározása")

def lnko(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
elso_szam = int(input("a: "))
masodik_szam = int(input("b: "))
print(f"A két szám legkisebbb közös többszöröse {lkkt(elso_szam, masodik_szam)}")
print(f"A két szám legnagyobb közös osztója {lnko(elso_szam,masodik_szam)}")
