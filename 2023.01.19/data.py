class eredmeny:
    def __init__(self, sor:str):
        adatok=sor.strip().split(" ")
        self.helyezes = int(adatok[0])
        self.letszam = int(adatok[1])
        self.sportag = adatok[2]
        self.versenyszam = adatok[3]
    
    def pont(self):
        if self.helyezes == 1:
            return 7
        elif self.helyezes == 2:
            return 5
        elif self.helyezes == 3:
            return 4
        elif self.helyezes == 4:
            return 3
        elif self.helyezes == 5:
            return 2
        else:
            return 1

eredmenyek:list[eredmeny] = []