from model import Igra, novaigra

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = "W"
PORAZ = "X"

def izpis_igre(igra: Igra):
    return igra.pravilni_del_gesla

def izpis_zmage(igra: Igra):
    return ZMAGA


def izpis_poraza(igra: Igra):
    return PORAZ 

