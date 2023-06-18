class hegy:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.hegycsucs = adatok[0]
        self.hegyseg = adatok[1]
        self.magassag = adatok[2]

from typing import List
hegyek:List[hegy] = []