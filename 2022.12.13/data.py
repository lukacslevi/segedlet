class Varos:
    def __init__(self, sor:str):
        darabok=sor.strip().split(";")
        self.Nev = darabok[0]
        self.Orszag = darabok[1]
        self.Lakossag = int(darabok[2])