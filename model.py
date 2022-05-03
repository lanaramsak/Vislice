from ast import alias


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo: str, crke: list = []):
        self.geslo = geslo.upper
        self.crke = crke

    def napacne_crke(self):
        napacne = [crka for crka in self.crke if crka not in self.geslo]
        return napacne

    def pravilne_crke(self):
        pravilne = [crka for crka in self.crke if crka in self.geslo]
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(self.geslo) == len(self.pravilne_crke)

    def poraz(self):
        return len(self.napacne_crke) > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        izpis = ""
        for crka in self.geslo:
            if crka in self.crke:
                izpis += "crka"
            else:
                izpis += "_"
        return izpis
        #"".join(crka if crka in self.crke else "_" for crka in self.geslo)
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke)
    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open("besede.txt", encoding="utf8") as d:
    bazen_besed = d.read().split("\n")

# ali
# with open("besede.txt", encoding="utf8") as d:
#     for beseda in f:
#         bazen_besed.append(beseda.strip())

import random

def novaigra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)
    #prej smo dali crke za prevzeto vrednost []
