def atment(osszesDb, bukottDb):
    szazalek = (1-bukottDb/osszesDb) * 100
    return szazalek

osszes = int(input("összes tanulók száma:"))
bukott = int(input("Bukott tanulók száma:"))
szazalek = atment(osszes, bukott)
if szazalek < 0:
    print("hibás adat")
else:
    print(f"{szazalek} % ment át")

