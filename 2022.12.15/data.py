class Szakasz:

    def __init__(self,sor:str) -> None:
        adatok=sor.strip().split(";")
        self.indulas = adatok[0]
        self.erkezes = adatok[1]
        self.tavolsag = float(adatok[2].replace(",", "."))
        self.emelkedes = int(adatok[3])
        self.lejtes = int(adatok[4])
        self.pecseteloHely = (adatok[5]=="i")

    def HianyosNev(self):
        if self.pecseteloHely==True and "pecsetelohely" not in self.erkezes:
            return True
        else:
            return False


from typing import List
szakaszok:List[Szakasz]=[]