import math 

a = int(input('Kérem a másodfokú egyenlet fő együtthatóját'))
a = float(a)
while a == 0:
    print('ez nem lesz másodfokú egyenlet')
    a = int(input('Kérem a konstanst tagot'))
    a == float(a)

b = int(input('Kérem a másodfokú egyenlet fő együtthatóját'))
c = int(input('Kérem a konstans tagot'))
d = b*b-4*a*c
print(d)
if d >= 0:
    x1 = (-b+math.sqrt(d)/2*a)
    x2 = (-b+math.sqrt(d)/2*a)
    print(x1)
    print(x2)
    print('van valós megoldás')

else:
     x1 = (-b+math.sqrt(d)/2*a)
    x2 = (-b-math.sqrt(d)/2*a)
    print(x1)
    print(x2)
    print('nincs valós megoldás')