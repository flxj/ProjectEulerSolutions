from math import sqrt


#357  ##太暴力了，不行啊！！！
"""
def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
M=100000000
p357div=Divisors(M)
def isPrime_generating_integers(n):
    if isPrime(n+1):
        flag=True
        l=p357div.divisors(n)
        for i in range(1,len(l)//2+1):
            if isPrime(l[i]+l[len(l)-i-1])==False:
                flag=False
                break
        if flag:
            return True
        else:
            return False
    else:
        return False
r=0
for n in range(2,M,2):
    if isPrime_generating_integers(n):
        r+=n
print(r)
"""
###
#P389
"""
def p389():
    dice=[4,6,8,12,20]
    e,var=0.0,0.0
    ed,varsum=1.0,0.0
    for n in dice:
        E=lambda x:(x+1)/2.0
        Var=lambda x:(x**2-1)/12.0
        e,var=E(n),Var(n)
        varsum=varsum*e*e+var*ed
        ed*=e
    #return varsum
    print("%.4f" %(varsum))
"""
#p435
"""
def p435():
    mod=1307674368000
    def matrix_mult(A,B):
        n,m,h=len(A),len(B),len(B[0])
        ans=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(n):
            for j in range(m):
                for k in range(h):
                    ans[i][k]+=A[i][j]*B[j][k]
                    if ans[i][k]>=mod:
                        ans[i][k]%=mod
                    ans[i][k]%=mod
                ans[i][j]%=mod
        return ans
    def power(A,n,i):
        ans=[[0,i,i],[0,0,0],[0,0,0]]
        while n>0:
            if n &1 :
                ans=matrix_mult(ans,A)
            n>>=1
            A=matrix_mult(A,A)
        return ans[0][2]
    res=0
    for i in range(101):
        A=[[0,0,i**2],[0,1,1],[1,0,i]]
        res+=power(A,10**15-1,i)
    print(res%mod)
"""
#p506
p=[1,2,3,4,3,2]
d={0:""}
for i in range(6):
    d[sum(p[:i+1])]="".join(map(str,p[:i+1]))

#该函数以字符串形式返回Vn的值，太大的n会造成内存溢出问题
"""
def Vn(n):
    s=(n-1)*n//2
    m=s//15
    r=s%15
    if r==0:
        a=n//15
        b=n%15
        return "123432"*a+d[b]
    else:
        if (n+r)>=15:
            a=(n+r-15)//15
            b=(n+r-15)%15
            i=len(d[r])
            return d[15][i:]+"123432"*a+d[b]
        else:
            i=len(d[r])
            for j in range(i+1,7):
                if sum(p[i:j])==n:
                    return d[15][i:j]
"""
"""
v = [1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, 43212, 34321, 23432, 123432]
w = [234321, 343212, 432123, 321234, 123432, 432123, 212343, 432123, 123432, 321234, 432123, 343212, 234321, 123432, 123432]

M = 123454321

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

M1 = modinv(10 ** 6 - 1, M)
M2 = modinv((10 ** 6 - 1)**2, M)

def s(n):
    s = 0
    for p in range(len(v)):
        k = (n - p - 1) // 15

        if p >= n:
            break

        f = pow(10, 6*k + 6, M) - 1

        a = f * M1
        b = f * M2 - (k + 1) * M1

        s += a*v[p] + b*w[p]
    return s % M
#print(s(10 ** 14))
"""
#p504
"""
def points(a,b,c,d):
    res=a+b+c+d-3
    for i in range(1,c+1):
        m,n=(c-i)*b/c,int((c-i)*b/c)
        p,q=(c-i)*d/c,int((c-i)*d/c)
        if m==n:
            res+=n-1 if n>0 else 0
        else:
            res+=n
        if p==q:
            res+=q-1 if q>0 else 0
        else:
            res+=q

    for i in range(1,a+1):
        m,n=(a-i)*b/a,int((a-i)*b/a)
        p,q=(a-i)*d/a,int((a-i)*d/a)
        if m==n:
            res+=n-1 if n>0 else 0
        else:
            res+=n
        if p==q:
            res+=q-1 if q>0 else 0
        else:
            res+=q
    return res
"""
"""
##可行，但是太暴力
from eulerlib import gcd
M=100
gc=[[0 for i in range(M+1)] for j in range(M+1)]
for i in range(1,M+1):
    for j in range(i,M+1):
        gc[i][j]=i*j-gcd(i,j)
        gc[j][i]=i*j-gcd(i,j)
res=0
for a in range(1,M+1):
    for b in range(1,M+1):
        for c in range(1,M+1):
            for d in range(1,M+1):
                n=(gc[a][b]+gc[b][c]+gc[c][d]+gc[d][a])//2+1
                if sqrt(n)==int(sqrt(n)):
                    res+=1

print(res)

"""
#p346
"""
N=10**12
def p346(N):
    res=set()
    k=2
    while k<N:
        n=0
        while n<N:
            if n>k+1:
                res.add(n)
            n=n*k+1
        k+=1
    return sum(res)+1
print(p346(N))
"""
#p549
""""
from eulerlib import primes
from eulerlib import Divisors
M=100
div=Divisors(M)
pres=primes(M)

def fac(n):
    res={}
    for p in pres:
        if p>n:
            break
        res[p]=0
        q=p
        while q<n:
            res[p]+=n//q
            q*=p
    return res

def isprime(n):
    i,j=0,len(pres)-1
    while i<j:
        mid = (i + j) // 2
        if n < pres[mid]:
            j=mid-1
        elif n == pres[mid]:
            return True
        else:
            i=mid+1
    return n==pres[i]
def f(pn,fa):
    for p in pn:
        if p[0] not in fa or fa[p[0]]<p[0]:
            return False
    return True
def s(n):
    pn=div.prime_factors(n)
    if len(pn)==1:
        return n
    for m in range(pn[-1][0],n+1):
        if f(pn,fac(m)):
            return m
    return 0
def S(n):
    res=0
    for i in range(2,n+1):
        res+=s(i)
    return res
print(S(M))
"""
#304
"""
from math import sqrt
from eulerlib import primes
BASE=10**14
RANGE=10000000
MOD=1234567891011

comp=[False]*RANGE
pres=primes(int(sqrt(BASE+RANGE)))
for p in pres:
    for i in range((BASE+p-1)//p*p-BASE,len(comp),p):
        comp[i]=True
def next_prime(n):
    while True:
        n+=1
        if n>=len(comp):
            raise AssertionError("motherfucker")
        if not comp[n]:
            return n
def fib_mod(n,m):
    a,b=0,1
    binary=bin(n)[2:]
    for bit in binary:
        a,b=a*(b*2-a),a*a+b*b
        if bit=='1':
            a,b=b,a+b
        a%=m
        b%=m
    return a
res=0
p=0
for i in range(100000):
    p=next_prime(p)
    res=(res+fib_mod(BASE+p,MOD))%MOD
print(res)
"""
#307
print(18/49)













