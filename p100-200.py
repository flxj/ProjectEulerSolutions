#import itertools
#import eulerlib
#import math
#
#101
"""
import  numpy as np
def u(n):
    sign=-1
    u=1
    for i in range(10):
        u=u*n+sign
        sign*=-1
    return u
def u_generator(N):
    n=1
    while n<=N:
        yield u(n)
        n+=1

#def U2(n):
#    return n**10-n**9+n**8-n**7+n**6-n**5+n**4-n**3+n**2-n+1
#[1, 683, 44287, 838861, 8138021, 51828151, 247165843, 954437177, 3138105961, 9090909091]
"""





#102
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
"""
# Returns the tuple (F(n), F(n+1)), computed by the fast doubling method.
def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
def compute():
    MOD = 10**9
    a = 0
    b = 1
    for i in itertools.count():
        if "".join(sorted(str(a))) == "123456789":  # If suffix is pandigital
            f = fibonacci(i)[0]
            if "".join(sorted(str(f)[ : 9])) == "123456789":  # If prefix is pandigital
                return str(i)
        a, b = b, (a + b) % MOD
    return str(ans)
print(compute())
"""
#108

"""
def count_divs(n):
    cnt=1
    end=int(math.sqrt(n))
    for i in itertools.count(2):
        if i>end:
            break
        if n%i==0:
            j=0
            while True:
                n//=i
                j+=1
                if n%i!=0:
                    break
            cnt+=2*j+1
            end=int(math.sqrt(n))
    if n!=1:
        cnt*=3
    return cnt
for  n in itertools.count(1):
    if(count_divs(n)+1)//2>1000:
        print(n)
        break

"""
#p115
"""
def p115():
    M=50
    ways=[1]
    for n in itertools.count(1):
        s=ways[n-1]+sum(ways[:max(n-M,0)])
        if n>=M:
            s+=1
        ways.append(s)
        if s>1000000:
            return n
print(p115())
"""
#118


#123
"""
p=eulerlib.primes(1000000)
for n in range(5,len(p),2):
    m=n*p[n-1]*2
    if m>10000000000:
        print(str(n))
        break
"""
#124
"""
from eulerlib import Divisors
from functools import reduce
N=100000
Div=Divisors(N)

rad=[]
for n in range(1,N+1):
    rad.append((n,reduce(lambda x,y:x*y,Div.prime_factors_only(n),1)))

rad.sort(key=lambda x:x[1])

print(rad[9999][0])
"""






#126
#计算第K层所需立方体数目
from eulerlib import primes
def cubes(x,y,z,k):
    return 2*(x*y+y*z+x*z)+4*(k-1)*(x+y+z+k-2)

#暴力版C(n)
"""
def C(n):
    m=int(n/2-2)
    r1,r2,r3=0,0,0
    for x in range(1,m+1):
        for y in range(1,m+1):
            for z in range(1,m+1):
                k=1
                while True:
                    if cubes(x,y,z,k)>n:
                        break
                    elif cubes(x,y,z,k)==n:
                        if x==y and y==z:
                            r1+=1
                        elif x!=y and y!=z and x!=z:
                            r2+=1
                        else:
                            r3+=1
                    k+=1
    return r1+r2//6+r3//3
"""
def cl(lv,d1,d2,d3):
    return 2*(d1*d2+d1*d3+d2*d3)+(d1+d2+d3+lv-2)*4*(lv-1)
#-------------------------------------------
"""
def fun(cubes):
    l=[0 for i in range(cubes+1)]
    ct=0;mx=0
    for d1 in range(1,cubes):
        if cl(1,d1,d1,d1)>cubes:
            break
        for d2 in range(d1,cubes):
            if cl(1,d1,d2,d2)>cubes:
                break
            for d3 in range(d2,cubes):
                if cl(1,d1,d2,d3)>cubes:
                    break
                for lv in range(1,cubes):
                    k=cl(lv,d1,d2,d3)
                    if k>cubes:
                        break
                    l[k]+=1
    return l
#-------------------------------------------
q=1000; m=20; cube=q*m

qs=fun(cube)
res=min([i for i in range(len(qs)) if qs[i]==q])
print(res)
"""

#127
#太暴力了，不行！！！
"""
from functools import reduce
from eulerlib import gcd
from eulerlib import Divisors

M=120000
Div=Divisors(M)

pf={}
for i in range(1,M+1):
    pf[i]=Div.prime_factors_only(i)

def Gcd(a,b):
    for p in pf[a]:
        if p in pf[b]:
            return 0
    return 1


def rad(n):
    #res=reduce(lambda x,y:x*y,Div.prime_factors_only(n),1)
    res = reduce(lambda x, y: x * y, pf[n], 1)
    return res

def abc_hits():
    res=0
    for a in range(1,M//2+1):
        for b in range(a+1,M-a):
            if Gcd(a,b)==1:
                if Gcd(a,a+b)==1 and Gcd(b,a+b)==1:
                    if rad(a)*rad(b)*rad(a+b)<a+b:
                        res+=a+b
    return res
print(abc_hits())
"""
#132
"""
from eulerlib import is_prime
import itertools
def compute():
    cond = lambda i: is_prime(i) and repunit_mod(10**9, i) == 0
    ans = sum(itertools.islice(filter(cond, itertools.count(2)), 40))
    return str(ans)

def repunit_mod(k, m):
    return (pow(10, k, m * 9) - 1) // 9
print(compute())
"""
#133
#大神请收下我的膝盖吧！我太弱了
"""
from eulerlib import primes
def has_divisible_repuint(p):
    return (pow(10,10**16,p*9)-1)//9%p==0

def p133():
    P = primes(10**5)
    res=sum(p for p in P if p==2 or p==5 or not has_divisible_repuint(p))
    return res
print(p133())
"""

#135
#from eulerlib import Divisors
#from eulerlib import is_prime
#M=1000000
#Div=Divisors(M)
"""
def nums_of_solutions(n):
    if is_prime(n):
        return 0
    num=0
    d=Div.divisors(n)
    for i in range(len(d)):
        if i<len(d)//2:#需要m>z
            for z in range(1,d[i]//2+1):
                m=d[i]-z
                if 3*m-z==d[len(d)-i-1]:
                    num+=1
        else:#需要m<=z
            for m in range(1,d[i]//2+1):
                z=d[i]-m
                if 3*m-z==d[len(d)-i-1]:
                    num+=1
    return num

f=[False for i in range(M)]

def fill(n):
    i=1
    while i*i*n<M:
        f[i*i*n]=True
        i+=1
    return i-1
def p135():
    res=0
    for i in range(1,M):
        if not f[i] and nums_of_solutions(i)==10:
            res+=fill(i)
    return res
print(p135())
"""

"""
def pe135():
    LIMIT = 10 ** 6
    solutions = [0] * LIMIT
    for m in range(1, LIMIT * 2):
        for k in range(m // 5 + 1, (m + 1) // 2):
            temp = (m - k) * (k * 5 - m)
            if temp >= LIMIT:
                break
            solutions[temp] += 1

    ans = solutions.count(10)
    return str(ans)
print(pe135())


def PE135():
    M=10**6
    res=[0 for i in range(M)]
    for a in range(1,M+1):
        b=4-a%4
        while a*b<M and b<3*a:
            res[a*b-1]+=1
            b+=4
    ans=res.count(10)
    return ans
print(PE135())
"""
#138
###网上大神的解，连分式，叼啊！牛B！
"""
x,y=2,1
s,n=0,0
while n<12:
    x_=9*x+20*y
    y_=9*y+4*x
    x,y=x_,y_
    if x%5==2 or x%5==3:
        n+=1
        s+=y
print(s)
"""
#事实上有a(n) = Fibonacci(6*n+3)/2,太神奇了！！！
#print(sum([17, 305, 5473, 98209, 1762289, 31622993,
#           567451585, 10182505537, 182717648081,
#           3278735159921, 58834515230497, 1055742538989025]))

#146


#148
#这是别人的代码，大家怎么都这么吊！
"""
# triangular number
def t(n):
    return n * (n + 1) // 2

# representation of n in base b
def digits(n, b):
    res = []
    while n > 0:
        res.append(n % b)
        n = n // b
    return res


def count(n, b):
    dig = digits(n, b)
    res = 0
    for k in range(len(dig)):
        d = dig[k]
        res = t(d) * t(b) ** k + (d + 1) * res
    return res
print(count(10**9, 7))
"""
#151
"""
def p151(sizes=[1,1,1,1],mem={}):
    key=tuple(sizes)
    if key in mem:
        return mem[key]
    pages=sum(key)
    if not pages:
        return -1
    for i,n in enumerate(key):
        if not n:
            continue
        sizes[:i]=key
        for j in range(i,len(key)):
            sizes[j]+=1
        sizes[i]-=2
        mem[key]+=p151()*n/pages
    return mem[key]
print(p151())
"""
#164
"""
def digit_sum(n):
    return sum(int(c) for c in str(n))
def p164():
    BASE=10
    DIGITS=20
    CONSECUTIVE=3
    MAX_SUM=9

    n=BASE**CONSECUTIVE
    ways=[[1]+[0]*(n-1)]

    for d in range(1,DIGITS+CONSECUTIVE+1):
        newrow=[]
        for p in range(n):
            s=0
            if digit_sum(p)<=MAX_SUM:
                for nex in range(BASE):
                    s+=ways[d-1][p % (BASE ** (CONSECUTIVE - 1)) * BASE + nex]
            newrow.append(s)
        ways.append(newrow)
    ans=ways[-1][0]-ways[-2][0]
    return str(ans)
print(p164())
"""
#173
"""
M=10**6
laminas=set()
for a in range(4,M,2):
    for b in range(2,a,2):
        if a*b>M:
            break
        laminas.add((a+b,a-b))
print(len(laminas))
"""
#174
"""
M=10**6
laminas=set()
count=[0 for i in range(M)]

for a in range(4,M,2):
    for b in range(2,a,2):
        if a*b>=M:
            break
        if (a+b,a-b) not in laminas:
            count[a*b]+=1
        laminas.add((a + b, a - b))
s=0

for i in range(M):
    if count[i]>=1 and count[i]<=10:
        s+=1
print(s)

"""
#179
"""
def p179():
    div=[2]*(10**7+1)
    for i in range(2,(len(div)+1)//2):
        for j in range(i*2,len(div),i):
            div[j]+=1
    ans = sum((1 if div[i] == div[i + 1] else 0) for i in range(2, len(div) - 1))
    return str(ans)
print(p179())
"""
#187
"""
from eulerlib import primes
M=10**8
p=primes(M//2)

res=0
a=[True for i in range(M)]
for i in range(len(p)):
    for j in range(i,len(p)):
        if p[i]*p[j]<M:
            res+=1
        else:
            break
print(res)
#17427258
"""
#188
#这不是我写的
"""
from math import  sqrt
import  sys

def totient(n):
    assert n>0
    p=1
    i=2
    end=int(sqrt(n))
    while i<=end:
        if n%i==0:
            p*=i-1
            n//=i
            while n%i==0:
                p*=i
                n//=i
            end=int(sqrt(n))
        i+=1
    if n!=1:
        p*=n-1
    return p


def tetration_mod(x,y,m):
    if y==1:
        return x%m
    else :
        return pow(x,tetration_mod(x,y-1,totient(m)),m)

x,y,m=1777,1855,10**8
sys.setrecursionlimit(y+30)
res=tetration_mod(x,y,m)
print(res)
"""


#191 又是人家的代码
"""
def stretched_fibo_gen(steps=None):
    #Generate the sequence members of a generalized fibonacci sequences.

    #For a list of steps [i,j,...,k,l], the next sequence member F_n is defined as
    #    F_n = F_(n-i) + F_(n-j) + ... + F_(n-k) + F_(n-l)
    #The initial set of values is a list of zeros and in a single 1 such that there
    #are max(steps) initial values, and that there are min(steps) ones.

    #:param steps: list of int
    #:yield: int

    if not steps:
        steps = [1,2]
    steps.sort()

    furthest_back = max(steps)
    starting_ones = min(steps)
    starting_zeros = furthest_back - starting_ones
    fib = [0] * starting_zeros + [1] * starting_ones
    for starting in fib:
        yield starting

    while True:
        fib.append(sum([fib[-i] for i in steps]))
        yield fib[-1]
        fib =  fib[-furthest_back:]


def cost(n):
    #Define the q219 cost function abstractly

    #The basic form of this identity is,
    #if n = 1 + F_0 + ... + F_m, then cost(n) = F_0 * 0 + ... F_m * m.
    #That is, m is difference between consecutive costs F_m times.

    #If n is between summands of F_i, then j is used to adjust the number times m is added.

    if n == 1:
        return 1
    elif n <= 0:
        return 0

    N = n - 1
    stretched_fibo = [0, 0]  # add extra zeros to line up indices so F_i * i is added
    for idx, fm in enumerate(stretched_fibo_gen([1, 4])):
        N -= fm
        if N <= 0:
            stretched_fibo.append(fm + N)
            break
        else:
            stretched_fibo.append(fm)

    return sum([idx * fm for idx, fm in enumerate(stretched_fibo)])


def C(N):
  m, n,D, a,b,c,d = 0, 1,0, 1,0,0,0
  while n<N:
    if N-n <= a:a = N-n

    #m, n,D, a,b,c,d  +=  m+1,  n+a, D+a*m,  a+b,c,d,a
    m+=m+1
    n+=n+a
    D+=D+a*m
    a+=a+b
    b+=c
    c+=d
    d += a
  return 5*N-5+D
print(C(10**9))
"""
#203
"""
from eulerlib import nCr
from eulerlib import Divisors

M=50
div=Divisors(M)

def is_squarefree(n,r):
    if r==0 or r==n:
        return True
    p=[0 for i in range(n+1)]
    for i in range(n,n-r,-1):
        for t in div.prime_factors(i):
            p[t[0]]+=t[1]
    for i in range(2,r+1):
        for t in div.prime_factors(i):
            p[t[0]]-=t[1]
    return not any(map(lambda x:x>=2,p))

def pe203():
    res=set()
    for n in range(1,M+1):
        for r in range(0,n+1):
            if is_squarefree(n,r):
                res.add(nCr(n,r))
    return int(sum(res))
"""

#204
"""
from eulerlib import primes
M=10**9
prime=primes(100)

def count(primeidx,product):
    if primeidx==len(prime):
        return 1 if product<=M else 0
    else:
        res=0
        while product<=M:
            res+=count(primeidx+1,product)
            product*=prime[primeidx]
        return res

print(count(0,1))
##另一个人的方法
end = 10**9
def doIt(setin,mul):
    s = set()
    for y in setin:
        z = y
        while z <end:
            s.add(z)
            z*=mul
    return s
s=set()
s.add(1)
for x in prime:
    s = doIt(s,x)
print(len(s))
"""
#231
from eulerlib import Divisors
from eulerlib import primes
N=20000000
M=15000000
















