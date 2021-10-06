OLVADAS = int(input('Mennyi az olvadási pont?'))
FORRAS = int(input('Mekkora a forráspontja?'))

OLVADAS = 1539
FORRAS = 2750
hofok =  int(input('Hőfok:'))
if hofok < OLVADAS:
    print('Szilárd')
elif hofok < FORRAS:
    print('folyékony')
else: 
    print('Gáz')