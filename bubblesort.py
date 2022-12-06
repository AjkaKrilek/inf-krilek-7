import random
def zoznamik(zoznam):
    a = len(zoznam)
    b = len(zoznam)
    while b>0:
        for a in range(a-1):
            if zoznam[c]>zoznam[c+1]:
                zoznam[c], zoznam[c+1] = zoznam[c+1], zoznam[c]
            elif zoznam[c]<zoznam[c+1] :
                zoznam[c], zoznam[c+1] = zoznam[c], zoznam[c+1]
        b=b-1
    return zoznam
zoznam=[]
for i in range(10):
    zoznam.append(random.randrange(0,100))
print(zoznamik(zoznam))
