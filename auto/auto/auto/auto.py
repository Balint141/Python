
auto = input('Egy autónév rendel!')
vegsebesseg = int(input('Mi a végsebessége a(z) ' + auto + '-nek' + '? '))
anyag = int(input('Mivel megy a(z) ' + auto + '?' ))
orszag = input('Hol készül a(z) ' + auto + '?')
mondat2 = '{} készül a {} ami {} km/h végsebességre képes és {} -el megy'.format(orszag,auto,vegsebesseg,anyag) 
print(mondat2)

 
