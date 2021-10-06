nev = input('Mi a neve?')
bogyo = int(input('Kérem adja meg hogy mennyi bogyót gyüjtött'))

if bogyo < 10:
    minosites = 'Zsenge'
elif bogyo > 20:
    minosites = 'nagy koponya'
else:
    minosites = 'gyűjtögető'
print(f'{nev} egy {minosites}.')