#243
#又又又又是大神的代码，我copy代码已经到了“丧心病狂”的程度了！！！老天啊，赐予我智慧吧！！！
"""
from eulerlib import is_prime
from fractions import  Fraction
def p243():
    R=Fraction(15499,94744)
    totient,denominator=1,1
    p=2
    while True:
        totient*=p-1
        denominator*=p
        while True:
            p+=1
            if is_prime(p):
                break
        if Fraction(totient,denominator)<R:
            for i in range(1,p):
                numer=i*totient
                denom=i*denominator
                if Fraction(numer,denom-1)<R:
                    return str(denom)
print(p243())
"""

##282
#太暴力了，不行.
"""
#递归阿克曼函数
def Ackermann1(m,n):
    if m==0:
        return n+1
    else:
        if n==0:
            return Ackermann1(m-1,1)
        else:
            return Ackermann1(m-1,Ackermann1(m,n-1))
#非递归
def Ackermann2(m,n):
    ack=[[m,n]]
    while True:
        if len(ack)>0:
            t=ack[len(ack)-1]
            if t[0]==0:
                if len(ack)==1:
                    return t[1]+1
                else:
                    ack[len(ack)-2][1]=t[1]+1
                    ack.pop()
            elif t[1]==0:
                t[0]-=1
                t[1]=1
            else:
                l=[t[0],t[1]-1]
                t[0]-=1
                t[1]=-1
                ack.append(l)
a=[[0 for x in range(7)] for y in range(7)]
for m in range(4):
    for n in range(7):
        a[m][n]=Ackermann2(m,n)
"""
#287

#443
"""
An observation, which can lead to a fast solution without factorizing: 
numbers where gcd<>1 form clusters, and if the last number in a cluster is n, 
then the next cluster begins with 2n−1.
"""
"""
from PElib import is_prime
from eulerlib import gcd
def p443_1(n):
    def find_stop(n):
        g=3*n
        while True:
            n+=1
            x=gcd(n,g)
            if n%3==0 and x>1 and is_prime(2*n-1):
                return n
            else:
                g+=gcd(n,g)
    start,stop=17,21
    while stop<n/2:
        start=2*stop-1
        stop=find_stop(start)
    return 2*stop+n
def p443_2(x):
    n=17
    k=51
    while True:
        if is_prime(2*n-1):
            k=n-1
        else:
            k=1
            while (2*n-1)%(2*k+1):
                k+=1
        n+=k
        if x<=n:
            return 2*(n-k)+x
"""

#p371
"""
x = y = 0
for i in range(500):
    y = (1+0.002*i*y)/(0.5+i*0.001)
    x = (1+0.002*i*x+0.001*y)/(0.5+i*0.001)

print ("%.8f"%x)
"""
#p303
"""
from queue import Queue
def small_digits(n):
    return all(int(s)<=2 for s in str(n))


p=[[] for i in range(10)]
for i in range(1,10):
    for j in range(1,10):
        if i*j%10<=2:
            p[i].append(j)
def p303(x):
    r=[False for i in range(10010)]
    if x<3:
        return 1
    q=Queue()
    q.put((1,1))
    q.put((2,2))
    r[1],r[2]=True,True
    while True:
        t=q.get()
        n,m=t[0],t[1]
        if m==0:
            return n//x
        for i in range(3):
            mn=(m*10+i)%x
            if not r[mn]:
                r[mn]=True
                q.put((n*10+i,mn))
res=0
for i in range(1,10001):
    res+=p303(i)
print(res)
"""


"""
def f(n):
    if n == 9999: return 11112222222222222222
    fn = n
    OK = False
    while not OK:
        strfn = str(fn)
        OK = True
        for i in range(len(strfn)):
            if not strfn[i] in ['0', '1', '2']:
                OK = False
                p = 10 ** (len(strfn) - i - 1)
                minfn = ((fn // p) + 1) * p
                fn = ((minfn - 1) // n + 1) * n
                break
    return fn


def euler303(nmax):
    s = 0
    for n in range(nmax):
        s += f(n + 1) // (n + 1)
    return s
print(euler303(10000))
"""
#381








