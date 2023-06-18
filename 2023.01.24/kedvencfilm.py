def óraperc(perc):
    óra = perc // 60
    perc -= óra * 60
    return str(óra) + " óra" + str(perc) + " perc"

for i in range(3):
    cim = input("Add meg a film címét! ")
    hossz = int(input("Hány perces a film?"))
    print(f"A {cim} című film {óraperc(hossz)}")