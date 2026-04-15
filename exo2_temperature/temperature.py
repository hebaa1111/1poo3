class Temperature:
    def __init__(self, valeur_celsius):
        if isinstance(valeur_celsius, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(valeur_celsius, (int, float)):
            raise TypeError("Doit être un nombre")
        if valeur_celsius < -273.15:
            raise ValueError("Sous le zéro absolu")

        self._valeur_celsius = valeur_celsius

    @property
    def valeur_celsius(self):
        return self._valeur_celsius

    @property
    def fahrenheit(self):
        return (self._valeur_celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._valeur_celsius + 273.15

    @property
    def etat(self):
        if self._valeur_celsius <= 0:
            return "solide"
        elif self._valeur_celsius < 100:
            return "liquide"
        return "gazeux"

    @classmethod
    def depuis_fahrenheit(cls, valeur_f):
        return cls((valeur_f - 32) * 5/9)

    def est_compatible_avec(self, autre):
        return self.etat == autre.etat