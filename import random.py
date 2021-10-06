import random
egyik = random.randint(1,10)
masik = random.randint(1,10)
osszeg = egyik+masik
if osszeg%2 == 0:
    print('Páros')
    if osszeg%3 == 0:
        print('osztható 3-mal')
    else:
        print('Nem osztható 3-mal')
else:
    print('páratlan')
