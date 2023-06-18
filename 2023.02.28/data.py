class Pilota:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.szul = adatok[1]
        self.nemzetiseg = adatok[2]
        self.rajtszam = adatok[3]
        if self.rajtszam != "":
            self.rajtszam = int(self.rajtszam)

pilotak:list[Pilota] = []

        
