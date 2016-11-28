"""Akarmi"""
def szetvago(szoveg):
    """ kovetkezo faszsag """
    file_ = open(szoveg).read()
    output_szoveg = str()
    for word in file_.split('.'):
        output_szoveg.join(word)
    return output_szoveg

def mondatokra(szoveg):
    """cukorral kave"""
    mondatok = []
    for punct in ".?":
        szoveg = szoveg.strip().replace(punct, "!")
    for mondat in szoveg.split("!"):
        if mondat.strip():
            mondatok.append(mondat.strip())
    return mondatok

def szavakra(mondat):
    """bele eper cukorral kave"""
    szavak = mondat.split()
    strippelt_szavak = []
    for szo in szavak:
        strippelt_szavak.append(szo.strip(",.()"))
    return strippelt_szavak

def feldolgoz(fajl):
    """feldolgoz kave"""
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        kimenet.append(szavak)
    return kimenet

def joe(fajl):
    """cukorral kave"""
    kimenet = []
    szoveg = open(fajl).read()
    for mondat in mondatokra(szoveg):
        szavak = szavakra(mondat)
        for index in enumerate(szavak):
            if szavak[index].istitle() is True:
                szavak[index] = "Joe"
        kimenet.append(szavak)
    return kimenet
