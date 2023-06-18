def length(circuit): # Egészítse ki a függvényt a hiányzó formális paraméterrel!
    circuits = {}
    circuits['HUN'] = 4.381
    circuits['BEL'] = 7.004
    circuits['ITA'] = 5.793
    circuits['MON'] = 3.337
    lengthOfCircuit = circuits[circuit]
    # Egészítse ki a függvényt a visszatérést végző résszel!

    return lengthOfCircuit

def sebesseg(ido:str,hossz):
    darabolt = ido.split(":")
    korIdo = int(darabolt[0]) * 60 + int(darabolt[1]) + float(darabolt[2])/1000
    return hossz*1000/korIdo*3.6

palya = input("Válassza ki a pályát:")
for i in range(3):
    print(f"A(z) {i+1}. versenyző: ")
    versenyzoNev = input("\tNeve: ")
    versenyzoIdo = input("\tIdő: ")
    print(f"{versenyzoNev} versenyző átlagsebessége: {sebesseg(versenyzoIdo, length(palya)):.2f} km/h")