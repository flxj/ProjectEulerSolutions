import itertools
import math
from eulerlib import primes
from eulerlib import  gcd
from math import factorial
def cni(n,i):
    return factorial(n)//factorial(i)//factorial(n-i)

def p(x):
    if x>2:
        return cni(7,x)*cni(9*x,20-x)*(pow(x,20-x)-x*factorial(x)*(pow(x-1,11-x)-1)/(x-2))/cni(70,20)
    else:
        return cni(7,2)/cni(70,20)
"""
#pe158
# select n from 26,and then select 2 from n--->"a1a2a3....ai...aj....an"
#if the length of "ai+1...aj-1" equ 0,then we have one way;then we have two ways
maxpn=0
for i in range(3,26):
    if maxpn<cni(26,i)*(2*cni(i,2)-i+1):
        maxpn=cni(26,i)*(2*cni(i,2)-i+1)
print(maxpn)
"""
"""
#p121
win=0
times=[x for x in range(1,16)]
for i in range(8,16):
    t1=0
    for item in itertools.combinations(times,i):
        t2=1
        for i in range(1,16):
            if i in item:
                t2*=1/(1+i)
            else:
                t2*=i/(1+i)
        t1+=t2
    win+=t1
print(int(1/win))
"""
"""
#p127
def rand(a,b,c):
    r=a*b*c
    s=1
    if a in plist:
        r=r//a
        s*=a
    if b in plist:
        r=r//b
        s*=b
    if c in plist:
        r=r//c
        s*=c
    i=0
    while plist[i]<=c//2:
        if r%plist[i]==0:
            s*=plist[i]
        i+=1
    return s
s=0
LIMIT=120000
plist=primes(LIMIT)

for c in range(LIMIT-1,1,-1):
    if c%2==0:
        for a in range(1,c//2,2):
            if gcd(a,c)==1 and gcd(c-a,c)==1 and gcd(c-a,a)==1:
                if rand(a,c-a,c)<c:
                    s+=c
    else:
        for a in range(1,c//2+1):
            if gcd(a, c) == 1 and gcd(c - a, c) == 1 and gcd(c - a, a) == 1:
                if rand(a, c - a, c) < c:
                    s += c

print(s)

"""
#p129,130
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
def getA(n):
    if n%2==0 or n%5==0:
        return 0
    else:
        k=1
        p=1
        s=1
        while s%n!=0:
            k+=1
            p=p*10%n
            s=s+p
        return k
"""
def p129():
    LIMIT=1000000
    t=1
    for n in itertools.count(LIMIT):
        if getA(n)>LIMIT:
            t=n
            break
    return t
print(p129())
"""
"""
def p130():
    num=[]
    for n in itertools.count(4):
        if len(num)<25:
            if isPrime(n)==False:
                if getA(n)!=0 and (n-1)%getA(n)==0:
                    num.append(n)
        else:
            break
    return sum(num)
print(p130())
"""
#131
