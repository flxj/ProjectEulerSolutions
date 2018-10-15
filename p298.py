import random
def insertL(l,n):
    if n in l:
        i=l.index(n)
        while i < len(l)-1:
            l[i]=l[i+1]
            i+=1
        l[len(l)-1]=n
        return 1
    else:
        if len(l)<5:
            l.append(n)
        else:
            i=0
            while i<len(l)-1:
                l[i]=l[i+1]
                i+=1
            l[len(l)-1]=n
        return 0
def insertR(r,n):
    if n in r:
        return 1
    else:
        if len(r)<5:
            r.append(n)
        else:
            i=0
            while i<len(r)-1:
                r[i]=r[i+1]
                i+=1
            r[len(r)-1]=n
        return 0
def onceGame(n):
    Lmemory=[]
    Rmemory=[]
    Lgrade=0
    Rgrade=0
    for i in range(n):
        num=random.randint(1,10)
        Lgrade+=insertL(Lmemory,num)
        Rgrade+=insertR(Rmemory,num)
    return abs(Lgrade-Rgrade)

def getE(n,m):
    dic = dict(zip(map(str, [x for x in range(m+1)]), [0 for i in range(m+1)]))
    for i in range(n):
        x=onceGame(m)
        dic[str(x)]+=1
    e=0.0
    for i in range(m+1):
        e+=i*dic[str(i)]/n
    return e


#print(getE(1000000,50))
"""
E=0.0
for i in range(400):
    E+=getE(1000,50)/400
print(E)

"""

