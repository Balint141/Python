JELSZO = 'Ezajojelszo'
jelszo=None
while jelszo != JELSZO:
    jelszo = input('Add meg a jelszvad')
    if  jelszo != JELSZO:
        print('Sajnos nem ez a jelszó próbáld újra!')
        pass
    print('Ez volt a jó jelszó ügyes vagy')