class eredmeny:
    def __init__ (self, sor:str):
        adatok=sor.strip().split(";")
        self.versenyzo = adatok[0]
        self.rajtszam = adatok[1]
        self.kategoria = adatok[2]
        self.versenyido = adatok[3]
        self.tavSzazalek = int(adatok[4])

eredmenyek:list[eredmeny] = []