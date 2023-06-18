class tanulo:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.szulev = int(adatok[0])
        self.osztaly = adatok[1]
        self.nev = adatok[2]

tanulok:list[tanulo] = []