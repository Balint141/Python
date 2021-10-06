""""
for x in range (101,1,-2):
    print (x)
"""
for x in range(2,101):
    for oszto in range(2,x/2+1):
        print(x,oszto)
        if (x%oszto) ==0:
            break
    else:
        print(x,"prím")