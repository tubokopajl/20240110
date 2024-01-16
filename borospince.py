class BorospinceException(Exception):

    def __init__(self, message):
        super().__init__(message)


class Bor:

    def __init__(self, fajta, evjarat, alkoholtartalom=12.5):
        self._fajta = fajta
        self._evjarat = evjarat
        self.alkoholtartalom = alkoholtartalom

    @property
    def fajta(self):
        return self._fajta

    @fajta.setter
    def fajta(self, value):

        self._fajta = value

    @property
    def evjarat(self):
        return self._evjarat

    @evjarat.setter
    def evjarat(self, value):
        self._evjarat = value

    @property
    def alkoholtartalom(self):
        return self._alkoholtartalom

    @alkoholtartalom.setter
    def alkoholtartalom(self, value):
        if not (0 <= value <= 100):
            raise BorospinceException("Nem megfelelo alkoholtartalom!")
        self._alkoholtartalom = value

    def __str__(self):
        return f"{self._fajta} (evjarat: {self._evjarat}), melynek alkoholtartalma: {self._alkoholtartalom}%"

    def __eq__(self, other):
        if isinstance(other, Bor):
            return (self._fajta.lower() == other._fajta.lower() and
                    self._evjarat == other._evjarat and
                    self._alkoholtartalom == other._alkoholtartalom)
        return False

class Szekreny:
    def __init__(self):
        self.borok = []

    def get_bor(self, n):
        if n < 0 or n >= len(self.borok):
            raise BorospinceException("Nem letezo index!")
        return self.borok[n]

    def __iadd__(self, bor):
        if not isinstance(bor, Bor):
            raise TypeError("Nem bor!")
        self.borok.append(bor)
        return self

    def __add__(self, other):
        if not isinstance(other, Szekreny):
            raise TypeError("Nem szekreny!")
        new_szekreny = Szekreny()
        new_szekreny.borok = self.borok + other.borok
        return new_szekreny

    def atlag_alkoholtartalom(self):
        if not self.borok:
            raise BorospinceException("Ures a szekreny!")
        return sum(bor._alkoholtartalom for bor in self.borok) / len(self.borok)

    def statisztika(self):
        return {fajta.lower(): sum(1 for bor in self.borok if bor._fajta.lower() == fajta.lower()) for fajta in set(bor._fajta for bor in self.borok)}

    def megisszak(self, bor):
        if not isinstance(bor, Bor):
            raise TypeError("Nem bor!")
        if bor not in self.borok:
            raise BorospinceException("Bor nem talalhato!")
        self.borok.remove(bor)

    def __str__(self):
        if not self.borok:
            return "Ez egy ures szekreny."
        stat = self.statisztika()
        return ", ".join(f"{count} {fajta}" for fajta, count in stat.items())
    

bor1 = Bor('tokaji aszu', 2017, 13.5)
bor2 = Bor('egri bikaver', 2013, 12.0)
bor3 = Bor('TOKAJI ASZU', 2015, 13.8)

szekreny = Szekreny()
szekreny += bor1
szekreny += bor2
szekreny += bor3

print(szekreny.get_bor(1))  

print(szekreny.atlag_alkoholtartalom())  

print(szekreny.megisszak(bor2))

print(szekreny.statisztika()) 

szekreny.megisszak(bor1) 

print(szekreny)  