import math
"""
def nextnum(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    return s

#p92
def getdigsum(n):
    s=0
    while n>0:
        s+=(n%10)**2
        n//=10
    return s
digsum=list(map(getdigsum,range(1000)))
def getconverge(n):
    r=0
    while True:
        if r==1 or r==89:
            break
        while n>0:
            r+=digsum[n%1000]
            n=n//1000
    return r

def p92():
    LIMIT=10000000
    cnt=0
    for n in range(2,LIMIT):
        if getconverge(n)==89:
            cnt+=1
    return cnt
print(p92())
"""
"""
#p99
def p99():
    maxnum=1
    maxline=1
    with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p099_base_exp.txt', 'r') as f:
        i=0
        while True:
            line = f.readline().strip()
            if len(line) > 1:
                i+=1
                s = list(line.split(','))
                if math.log(int(s[0]))*int(s[1])>maxnum:
                    maxnum=math.log(int(s[0]))*int(s[1])
                    maxline=i
            else:
                break
    return maxline
print(p99())
"""
#p97,逐次平方法求a**n mod m
"""
def prenum(n):
    i=0
    m=1
    while m<=n:
        i+=1
        m*=2
    return (i-1,m//2)
def sum2pow(n):
    l=[]
    while n>0:
        l.append(prenum(n)[0])
        n-=prenum(n)[1]
    return l
def list2pow(a,n,m):
    l=[]
    k=prenum(n)[0]
    i=0
    d=a%m
    while i<=k:
        l.append(d)
        i+=1
        d=d*d%m
    return l

def p97():
    m=pow(10,10)
    exp=7830457
    l=list2pow(2,exp,m)
    md=1
    for i in sum2pow(exp):
        md=md*l[i]%m
    return (md*28433+1)%m
print(p97())
"""
#print((28433*(2**7830457)+1)%10**10) 卧槽，这他妈直接就可以啊，shit!!!!

#p98
"""
##判断两个长为n的字符串是否互为重排 ####该方法存在问题！！！
wordnum=dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),[x for x in range(1,27)]))
def isAnagram(s1,s2,n):
    if s1[0] in s2:
        t1=0
        t2=0
        for i in range(n):
            t1+=wordnum[s1[i]]-wordnum[s1[0]]
            t2+=wordnum[s2[i]]-wordnum[s1[0]]
        if t1==t2:
            return True
        else:
            return False
    else:
        return False
##判断字符串s能否映射为数字n，若能则返回映射字典，否则返回空字典
def is_Replace_Ok(s,n):
    sn=str(n)
    d={}
    flag=True
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]]!=int(sn[i]):
                flag=False
                break
        else:
            d[s[i]]=int(sn[i])
    if flag:
        l=[0 for i in range(10)]
        for key in d:
            if l[d[key]]<1:
                l[d[key]]+=1
            else:
                return {}
        return d
    else:
        return {}
##判断两个长为n的字符串是否为重排平方数
def is_Anagramic_squares(s1,s2,n):
    if isAnagram(s1,s2,n):
        maxnum=0
        for i in range(int(math.sqrt(pow(10,n-1)))+1,int(math.sqrt(pow(10,n)))):
            m=0
            x=i*i
            d=is_Replace_Ok(s1,x)
            if len(d)!=0:
                if d[s2[0]]!=0:
                    for i in range(n):
                        m*=10
                        m+=d[s2[i]]
            if m!=0:
                if math.sqrt(m)==int(math.sqrt(m)):
                    if maxnum<max(x,m):
                        maxnum=max(x,m)
        return maxnum
    else:
        return 0

##将所有单词按长度组合字典
maxlen=0
words=dict(zip([x for x in range(1,21)],[[] for x in range(20)]))
with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p098_words.txt', 'r') as f:
        while True:
            line = f.readline().strip()
            if len(line) > 1:
                s = list(line.split(','))
                for w in s:
                    words[len(w)-2].append(w[1:-1])
                    if len(w)-2>maxlen:
                        maxlen=len(w)-2
            else:
                break
##找出最大平方数
n=maxlen
maxn=0
while n>1:
    if len(words[n])>1:
        for i in range(len(words[n])-1):
            for j in range(i+1,len(words[n])):
                m=is_Anagramic_squares(words[n][i],words[n][j],n)
                if maxn<m:
                    maxn=m
    if maxn!=0:
        break
    n-=1
print(maxn)

"""
#p66


#p75
"""
from eulerlib import gcd
L=1500000
C=[0 for i in range(L+1)]

def fill(x):
    i=1
    while x*i<=L:
        C[x*i]+=1
        i+=1

for m in range(2,L//2+1):
    n=1 if m%2==0 else 2
    while n<m:
        if gcd(m,n)==1:
            if 2*m*(m+n)<=L:
                fill(2*m*(m+n))
            else:
                break
        n+=2

res=0
for i in range(L+1):
    if C[i]==1:
        res+=1
print(res)

"""
#p86
"""
from math import sqrt
def isOK(a,b,c):
    n=0
    if a==max(a,b,c):
        n=(c+b)**2+a**2
    elif b==max(a,b,c):
        n=(a+c)**2+b**2
    else:
        n=(a+b)**2+c**2
    return True if int(sqrt(n))==sqrt(n) else False
"""

#156
##很明显，这些和我风格相左的代码，都是我扒的，自力更生，再扒剁手！！
"""
def countDigits(n, d):
    return str(n).count(str(d))

def count(n, d):
    if n<10:
        if n<d:
            return 0
        else:
            return 1
    else:
        return 10*count(n//10-1, d) + n//10 + countDigits(n//10, d)*(1+n%10) + count(n%10, d)

def log10(n):
    return len(str(n))

def getAll(d):

    n = 1
    s = 0
    while n<1000000000000:
        c = count(n, d)
        if c==n:
            s += n
            n += 1
        else:
            n += max(1, abs(n-c)//(2+log10(n)))
    return s

s=0
for d in range(1, 10):
    s += getAll(d)
print(s)
"""

#158
#p(n)=(2^n-n-1)*C(26,n)
#409511334375

#162
#大神们都用容斥原理解决。
#我直接暴力生成，结果悲剧了，搞了半天都不对，但我觉得此题暴力也可以，日后再想吧，我饿了，吃饭去。

#3D58725572C62302

#231
"""
#Legendre's formula
from PElib import list_smallest_prime_factors
M=20000000
N=15000000

P=list_smallest_prime_factors(M)
def prime_factor_sum(n):
    res=0
    for i in range(n+1):
        j=i
        while j>1:
            p=P[j]
            res+=p
            j//=p
    return res
res=prime_factor_sum(M)-prime_factor_sum(N)-prime_factor_sum(M-N)
print(res)
"""
#
#357
"""
from math import  sqrt
from eulerlib import  is_prime
from eulerlib import  primes
def Prime_generating_integer(n):
    if n%4==0 or sqrt(n)==int(sqrt(n)):
        return False
    for d in range(2,int(sqrt(n))+1):
        if n%d==0 :
            if not is_prime(d+n//d):
                return False
    return True
M=100000000

P=primes(M)
print("oooo")
res=0
for p in P:
    if Prime_generating_integer(p-1):
        res+=p-1
print(res)
"""

#134
#大神用中国剩余定理
"""""
from PElib import  list_primes
from PElib import reciprocal_mod
M=2000000
Primes=list_primes(M)
S=0
for i in range(2,len(Primes)):
    p1,p2=Primes[i],Primes[i+1]
    if p1>1000000:
        break
    k=1
    while k<p1:
        k*=10
    m=(p2-p1)*reciprocal_mod(k%p2,p2)%p2
    S+=m*k+p1
print(S)
"""
#169
"""
#Stern's diatomic series (or Stern-Brocot sequence)
#a(0) = 0, a(1) = 1; 
#for n > 0: a(2*n) = a(n), a(2*n+1) = a(n) + a(n+1). 
from math import log
def f(n):
    split, unsplit, gap = 0, 0, 0
    for i in range(1+int(log(n,2))):
        if n>>i&1 == 0: gap+=1
        else:
            if unsplit: unsplit, split = (1+gap)*unsplit + split, gap*unsplit + split
            else: unsplit, split = gap+1, gap
            gap = 0
    return unsplit
"""
#
#351
#a(n) = 6 * (C(n+1,2) - sum(i=1,n,phi(i)))

#387
from eulerlib import is_prime
"""
M=10**14
res=[0]
def find_hasd_prime(n,digsum,isstrong):
    m=n*10
    s=digsum
    for i in range(10):
        if m>=M:
            break
        if isstrong and is_prime(m):
            res[0]+=m
        if m%s==0:
            find_hasd_prime(m,s,is_prime(m//s))
        m+=1
        s+=1
for i in range(1,10):
    find_hasd_prime(i,i,False)
print(res[0])
"""
##
"""
def sumSRTHPRec(n, digitsum, limit):
    t=0
    for d in range(10):
        rtH = n*10 + d
        rtHdigitsum = digitsum + d
        if rtH > limit:
            return t
        if rtH % rtHdigitsum == 0:
            t+=sumSRTHPRec(rtH, rtHdigitsum, limit)
            if is_prime(rtH//rtHdigitsum):
                for i in [1,3,7,9]:
                    srtHp = rtH*10 + i
                    if srtHp > limit:
                        return t
                    if is_prime(srtHp):
                        t+=srtHp
    return t

def sumSRTHarshadPrimes(limit):
    return sum(sumSRTHPRec(h,h,limit) for h in range(1,10))

print (sumSRTHarshadPrimes(10**14))
"""































































































































































































