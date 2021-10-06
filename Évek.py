nev = input('Mi a neve?')
gyerek = int(input('Kérem adja meg a korát'))

if gyerek <= 13:
    minosites = 'Gyermek'
elif gyerek <= 17:
    minosites = 'Fiatalkorú'
elif gyerek <= 23:
    minosites = 'Ifjú'
elif gyerek <= 59:
    minosites = 'Felnőtt'
else: 
    minosites:'Idős' 
print(f'{nev} ön egy {minosites}.')