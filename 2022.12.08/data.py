class NobelDijas: 
    evszam=0
    tipus=""
    keresztnev=""
    vezeteknev=""

    def __init__(self,sor:str):
        darabok=sor.strip().split(";")
        self.evszam=int(darabok[0])
        self.tipus=darabok[1]
        self.keresztnev=darabok[2]
        self.vezeteknev=darabok[3]