import random
def bubblesort(zoz):
    a = len(zoz)
    for i in range(len(zoz)):
        for n in range(len(zoz)-1):
            if zoz[n]>zoz[n+1]:
                zoz[n],zoz[n+1]=zoz[n+1],zoz[n]
    return zoz
zoz=[]
for i in range(5):
    zoz.append(random.randrange(0,20))
print(bubblesort(zoz))
