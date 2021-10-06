tipus = input('Add meg a gép típusát')
allapota = True  if input('Működik (i/n)?') == 'i' else False
ar = int(input('Mennyibe kerül?'))
if (tipus == 'c64' or tipus == 'c64') and allapota and ar <=25000:
        print('ez pont önnek való')
else:
    print('Ez önnek nem felel meg')
