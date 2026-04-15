from temperature import Temperature

t1 = Temperature(22.5)
print(t1.fahrenheit)
print(t1.kelvin)
print(t1.etat)

t2 = Temperature.depuis_fahrenheit(32)
print(t2.valeur_celsius)

print(t1.est_compatible_avec(t2))

t3 = Temperature(50)
print(t1.est_compatible_avec(t3))

try:
    Temperature(-300)
except ValueError as e:
    print(e)

try:
    Temperature(True)
except TypeError as e:
    print(e)