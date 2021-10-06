nev = (input('Mi a neve?'))
gyerek = int(input('Hány pontot szerzett?'))
if gyerek <= 29:
    minosites = 'elégtelen(1)'
elif gyerek <= 37:
    minosites = 'elégésges(2)'
elif gyerek <= 43:
    minosites = 'közepes(3)'
elif gyerek <= 49:
    minosites = 'jó(4)'
elif gyerek <= 55:
    minosites = 'Jeles(5)'
print(f'{nev} ön  {minosites} értékelést szerzett.')
MINOSITES = 'Jeles(5)'
minosites=None
while minosites != MINOSITES:
    minosites = input('Add meg az osztályzatod')
    if  minosites != MINOSITES:
        print('Jeej ügyes vagy!')
        pass
    print('Sajnos nem ötös de majd máskor sikerül')
