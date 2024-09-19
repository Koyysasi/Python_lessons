class Jelolt:
    def __init__(self, vezeteknev, keresztnev, kerulet, szavazatok, tamogato):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.kerulet = kerulet
        self.szavazatok = szavazatok
        self.tamogato = tamogato
    def __str__(self):
        return f"[{self.vezeteknev} {self.keresztnev}] |{self.kerulet}| / {self.tamogato} Szavazatok: {self.szavazatok}"