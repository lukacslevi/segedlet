class Versenyzo:
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.hazai = adatok[0]
        self.idegen = adatok[1]
        self.hazai_pont = int(adatok[2])
        self.idegen_pont = int(adatok[3])
        self.helyszin = adatok[4]
        self.idopont = adatok[5]

versenyzok:list[Versenyzo] = []