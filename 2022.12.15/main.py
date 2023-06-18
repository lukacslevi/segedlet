from functions import *

kiinduloMagassag = fajlBeolvasas("kektura.csv")
print(f"Szakaszok száma: {len(szakaszok)}")
print(f"teljes hossza : {teljesHossz():.3f}")
print(f"\tKezdete: {szakaszok[legrovidebb()].tavolsag}")
print("hiányos állomásnevek: ")


van=False
for item in szakaszok:
    if item.HianyosNev():
        print("\t" + item.erkezes)
        van = True

if not van:
    print("\tNincs hiányos állomásnév")

print("A túra legmagasabban fekvő végpontja: ")
print(f"\tVégpont neve: {szakaszok[legmagasabb(kiinduloMagassag)].erkezes}\n\tA végpont tengerszint feletti magassága: {szakaszok[legmagasabb].celMagassag} m")

def fajlbaIras(induloMagassag):
    f=open("kektura2.csv", "w", encoding="UTF-8")
    f.write(induloMagassag+"\n")
    for item in szakaszok:
        f.write(f"{item.indulas};")
        if item.HianyosNev():
            f.write(f"{item.erkezes} pecsetelohely;")
        else:
            f.write(f"{item.erkezes};")

        f.write(f"{item.tavolsag};{item.emelkedes};{item.lejtes};{"i" if item.pecseteloHely else "n"}\n")


