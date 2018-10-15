from eulerlib import primes
from eulerlib import Divisors

from math import sqrt
import itertools

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
#43
"""
dig=[0,1,2,3,4,5,6,7,8,9]
p=[2,3,5,7,11,13,17]
def getnum(l,start,end):
    r=0
    while start<=end:
        r*=10
        r+=l[start]
        start+=1
    return r
def isSub_string_divisibility(s):
    for i in range(1,len(s)-2):
        if getnum(s,i,i+2)%p[i-1]!=0:
            return False
    return True
r=0
for n in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    if isSub_string_divisibility(n):
        r+=getnum(n,0,9)
print(r)
"""
#p44
""""
M=3000
p=[n*(3*n-1)//2 for n in range(M)]
s=set(p)
m=10**10
for i in range(1,M):
    for j in range(i+1,M):
        if p[i]+p[j] in s and p[j]-p[i] in s:
            if p[j]-p[i]<m:
                m=p[j]-p[i]
print(m)
"""

#p51

#M=1000000
#prime=primes(M)
"""
def replacements(n,t,l):
    cnt=0
    #l=len(str(n))
    for i in range(10):
        for j in t:
            a=n//pow(10,l-j)
            b=n%pow(10,l-j)
            n=((a//10)*10+i)*pow(10,l-j)+b
        if isPrime(n):
            cnt+=1
    return cnt

r=0
flag=False
n=1000001
while True:
    l=len(str(n))
    if l>1:
        for m in range(1,l):
            for t in itertools.combinations(list(range(1,l)),m):
                if replacements(n,t,l)>=8:
                    r=n
                    flag=True
                    break
            if flag:
                break
        if flag:
            break
    n+=2
print(r)
"""
#54
"""
from collections import Counter
poker=dict(zip(["2","3","4","5","6","7","8","9","10","J","Q","K","A"],range(13)))
rank=dict(zip(["High Card","One Pair","Two Pairs","Three of a Kind","Straight",
               "Flush","Full House","Four of a Kind","Straight Flush","Royal Flush"],range(10)))

def Sitiao_or_Hulu(values):
    val=values.most_common()
    val.sort(key=lambda  x:x[1],reverse=True)
    if val[0][1]==3:
        return "Full House",val
     return "Four of a Kind",val

def Santiao_or_Liangdui(values):
    val = values.most_common()
    val.sort(key=lambda x: x[1],reverse=True)
    if val[0][1] == 3:
        return "Three of a Kind", val
    return "Two Pairs", val

def Duizi(values):
    val = values.most_common()
    val.sort(key=lambda x: x[1],reverse=True)
    return "One Pair",val
def Shunzi_or_Danpai(values):
    val = values.most_common()
    val.sort(key=lambda x: poker[x[0]],reverse=True)
    if poker[val[-1][0]]-poker[val[0][0]]==4:
        return "Flush",val
    return "High Card",val


def what_rank(pokeres):
    values,color=Counter(),Counter()
    for p in pokeres:
        values.update(p[:-1])
        color.update(p[-1])
    m,n=len(values),len(color)
    if n==1:
        if m==2:
            r,val=Sitiao_or_Hulu(values) #四条或葫芦
            return rank[],val
        r,val=Shunzi_or_Danpai(values)
        if r=="Flush":
            if val[-1][0]=="A":#同花大顺
                return rank["Royal Flush"],val
            return rank["Straight Flush"],val  #同花顺
        return rank["Flush"],val      #同花

    else:
        if m==2:
            r, val = Sitiao_or_Hulu(values)  # 四条或葫芦
            return rank[r], val
        elif m==3:
            r, val = Santiao_or_Liangdui(values)  # 三条或两对
            return rank[r], val
        elif m==4:
            r, val = Duizi(values)  # 对子
            return rank[r], val
        else:
            r, val = Shunzi_or_Danpai(values)  # 顺子或单牌
            return rank[r], val
"""
"""
def compare(a,b):
    rank1,val1=what_rank(a)
    rank2,val2=what_rank(b)
    if rank1>rank2:
        return 1
    if rank1<rank2:
        return 2
    if rank1==9:#同为同花大顺
        return 3
    if rank1==1 or rank1==3:#对子或三条

    if rank1==2:#两对

    if rank1==5:#同为同花--->此情况最特殊

    else：
        #rank1==4 or rank1==8:同为顺子或同花顺
        #rank1==6 or rank1==7:同为葫芦或四条
"""






"""

with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p054_poker.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if len(line) > 1:
            cipther= [int(n) for n in list(line.split(','))]
        else:
             break
"""

#p59
"""
cipther=[]
with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p059_cipher.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if len(line) > 1:
            cipther= [int(n) for n in list(line.split(','))]
        else:
             break


def compute():
    bestkey = max(((x, y, z)
            for x in range(97, 123)  # ASCII lowercase 'a' to 'z'
            for y in range(97, 123)
            for z in range(97, 123)),
            key=lambda key: get_score(decrypt(cipther, key)))
    ans = sum(decrypt(cipther, bestkey))
    return str(ans)
def get_score(plaintext):
    result = 0
    for c in plaintext:
        if 65 <= c <= 90:  # ASCII uppercase 'A' to 'Z', good
            result += 1
        elif 97 <= c <= 122:  # ASCII lowercase 'a' to 'z', excellent
            result += 2
        elif c < 0x20 or c == 0x7F:  # ASCII control characters, very bad
            result -= 10
    return result
def decrypt(ciphertext, key):
    return [(c ^ key[i % len(key)]) for (i, c) in enumerate(ciphertext)]
print(compute())
"""
#61
####该程序有问题，错的
"""
def f(a,b,c):
    return int((-b+math.sqrt(b*b-4*a*c))/(2*a))
def p(e,n):
    if e==3:
        return n*(n+1)//2
    elif e==4:
        return n**2
    elif e==5:
        return n*(3*n-1)//2
    elif e==6:
        return n*(2*n-1)
    elif e==7:
        return n*(5*n-3)//2
    else:
        return n*(3*n-2)

r=[(),(),(),(f(1,1,-2000)+1,f(1,1,-20000)),(f(1,0,-1000)+1,f(1,0,-10000)),(f(3,-1,-2000)+1,f(3,-1,-20000)),
   (f(2,-1,-1000)+1,f(2,-1,-10000)),(f(5,-3,-2000)+1,f(5,-3,-20000)),(f(3,-2,-1000)+1,f(3,-2,-10000))]
d=[{},{},{},{},{},{},{},{},{}]
for i in range(3,8):
    for n in range(r[i][0],r[i][1]+1):
        t=p(i,n)
        if t<10000:
            if t%100>10:
                d[i][t//100]=t
                #d[i][t%100]=t


def isok(visited,rec,head,rear,a):
    flag=False
    nexta=0
    for e in range(3,8):
        if not visited[e]:
            if a in d[e] and a not in head:
                visited[e]=True
                rec[e]=d[e][a]
                head.add(a)
                rear.add(d[e][a]%100)
                nexta=d[e][a]%100
                flag=True
                break
    if flag:
        isok(visited,rec,head,rear,nexta)
    return
res=[]
for i in range(r[8][0],r[8][1]+1):
    visited=[True,True,True,False,False,False,False,False,False]
    rec=[0 for j in range(9)]
    head=set()
    rear=set()
    m=p(8,i)
    if m%100>10 and m//100<100:
        rec[8]=m
        visited[8]=True
        rear.add(m%100)
        #head.add(m//100)
        isok(visited,rec,head,rear,m%100)
        if all(visited) and (m//100 in rear):
            res=rec
            break
print(res,sum(res))
"""
########----28684----这又是我抄别人的代码，哎
"""
def test(num, idx):
    if idx == 3:
        t = (math.sqrt(1 + 8 * num) - 1) / 2
    elif idx == 4:
        t = math.sqrt(num)
    elif idx == 5:
        t = (math.sqrt(1 + 24 * num) + 1) / 6
    elif idx == 6:
        t = (math.sqrt(1 + 8 * num) + 1) / 4
    elif idx == 7:
        t = (math.sqrt(9 + 40 * num) + 3) / 10
    return t == int(t)


def figure(num, flag, idx):
    flag[idx] = num
    if flag.count(0) == 0 and (num%100) == (flag[5] // 100):
        print(flag, sum(flag))
        return
    for mowei in range(10, 100):
        nn = (num%100) * 100 + mowei
        for i in range(7, 2, -1):
            if flag[i - 3] == 0 and test(nn, i):
                figure(nn, flag, i - 3)
                flag[i - 3] = 0

for i in range(21, 22):
    Octagonal = i * (3 * i - 2)
    if (Octagonal%100) >= 10:
        figure(Octagonal, [0, 0, 0, 0, 0, 0], 5)

"""
#64




#65
"""
M=100
seq=[1 for x in range(M+1)]
k=1
while 3*k<=M:
    seq[3*k]=2*k
    k+=1
seq[0]-=1
seq[1]+=1
def get_nth_item(n):
    if n==1:
        return [seq[1],1]
    else:
        r=[seq[n],1]
        n-=1
        while n>=1:
            r[0]+=seq[n]*r[1]
            r[0],r[1]=r[1],r[0]
            n-=1
        r[0], r[1] = r[1], r[0]
        return r
s=0
for d in str(get_nth_item(100)[0]):
    s+=int(d)
print(s)
"""
#66
#求佩尔方程最小解









#70
##这。。。这。。。这。。。又是我网上扒的大神的代码，我写的太暴力了，不行了先哭会儿
"""
def test(i, j):
    k1 = sorted(list(str((i - 1) * (j - 1))))
    k2 = sorted(list(str(i * j)))
    return k1 == k2


# 筛选质数
T = 10000000
primelist = [1] * T
primelist[0] = primelist[1] = 0
for i in range(2, T):
    if primelist[i] != 1:
        continue
    for j in range(i * 2, T, i):
        primelist[j] = 0

idx = -1
minn = 9999999
for i in range(3, T, 2):
    if i > 3162:
        break
    if primelist[i] != 1:
        continue
    for j in range(i + 2, int(T / i), 2):
        if primelist[j] != 1:
            continue
        if test(i, j):
            if i * j / (i - 1) / (j - 1) < minn:
                minn = i * j / (i - 1) / (j - 1)
                idx = i * j
print(idx)
"""


#p74
"""
M=1000000
nn=[1 for x in range(10)]
for i in range(1,10):
    nn[i]=i*nn[i-1]
def nextnum(n):
    s=0
    for d in str(n):
        s+=nn[int(d)]
    return s
chain=list(map(nextnum,range(M)))
def getchain(n):
    l=[n]
    cnt=1
    nex=chain[n]
    while nex not in l:
        cnt+=1
        l.append(nex)
        if nex<M:
            nex=chain[nex]
        else:
            nex=nextnum(nex)
    return cnt
cnt=0
for n in range(1,M):
    if getchain(n)==60:
        cnt+=1
print(cnt)
"""
#71
"""
N=10**6
maxn,maxd=0,1
for d in range(1,N+1):
    n=3*d//7
    if d%7==0:
        n-=1
    if n*maxd>d*maxn:
        maxn,maxd=n,d
print(maxn)
"""
#p72
"""
import PElib
import  itertools

M=1000000
totients=PElib.list_totients(M)
res=sum(itertools.islice(totients,2,None))
print(res)
#303963552391
"""
#73
"""
from eulerlib import  gcd
#1/3<q/p<1/2--->2q<p<3q
M=12000
res=0
for q in range(2,M//2):
    for p in range(2*q+1,min(M,3*q)+1):
        if gcd(p,q)==1:
            res+=1
print(res)
"""
#75

#84


#86

#87
"""
MAX=50000000
pnum=primes(int(math.sqrt(MAX))+1)
cnt=0
num=[]
for i in pnum:
    if i*i<MAX:
        for j in pnum:
            if i*i+j*j*j<MAX:
                for k in pnum:
                    n=i*i+j*j*j+k*k*k*k
                    if n<MAX:
                        num.append(n)
                    else:
                        break
            else:
                break
    else:
        break
num.sort()
for i in range(len(num)-1):
    if num[i+1]-num[i]!=0:
        cnt+=1
print(cnt+1)
"""
#88
"""
maxk = 12000
n = [2 * maxk for i in range(maxk)]

def getpsn(num, sump, product, start):
    # print(num,' ',sump,' ',product)
    k = num - sump + product
    if k < maxk:
        if num < n[k]:
            n[k] = num
        for i in range(start, maxk // num * 2):  # 控制num<=2*maxk
            getpsn(num * i, sump + i, product + 1, i)


getpsn(1, 1, 1, 2)
ans = sum(set(n[2:]))
print(ans)
"""


#89
"""
rnum={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
rom=[1000,500,100,50,10,5,1]
def getroman(S):
    return rnum[S]
def roman(n):
    res=0
    while True:
        if n==0:
            break
        else:
            for p in rom:
                if p<=n:
                    res+=n//p
                    n%=p
                    break
    return res

def p89():
    res=0
    with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p089_roman.txt', 'r') as f:
        while True:
            line = f.readline().strip()
            if len(line) > 1:
                n=sum(map(getroman,line))
                res+=len(line)-roman(n)
            else:
                break
    return res
print(p89())
"""




