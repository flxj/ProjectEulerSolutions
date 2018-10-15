import itertools
import math
from eulerlib import  primes

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
#p11
"""
a_p11=['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',
'49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',
'81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',
'52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',
'22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
'24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
'32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
'67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
'24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
'21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
'78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
'16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
'86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
'19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
'04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
'88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
'04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',
'20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',
'20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',
'01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']
for i in range(len(a_p11)):
    s = list(a_p11[i].split(' '))
    l=[]
    for j in s:
        l.append(int(j))
    a_p11[i]=l
def maxPro(i,j,n):
    a=1
    b=1
    c=1
    d=1
    for k in range(n):
        a*=a_p11[i][j+k]
        b*=a_p11[i+k][j+k]
        c*=a_p11[i+k][j]
        d*=a_p11[i+n-k-1][j+k]
    return max(max(a,b),max(c,d))

def p11():
    N=20
    M=4
    maxpro=0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if maxpro<maxPro(i,j,M):
                maxpro=maxPro(i,j,M)
    return maxpro
print(p11())
"""
#p16
"""
s=0
for i in str(pow(2,1000)):
    s+=int(i)
print(s)
"""
#p17
"""
numwords=['one','two','three','four','five',
          'six','seven','eight','nine','ten',
          'eleven','twelve','thirtrrn','forthteen','fifteen',
          'sixteen','seventeen','eighteen','nineteen','twenty',
          'thirty','forty','fifty','sixty','seventy','eighty','ninety']
numdic=dict(zip([x for x in range(21)]+[30,40,50,60,70,80,90],[-3]+[len(x) for x in numwords]))
def lettercnt(n):
    s=0
    a=n//100
    b=n%100
    if (b//10)*(b%10)==0:
        s+=numdic[b]
    else:
        if b<20:
            s+=numdic[b]
        else:
            s+=numdic[b-b%10]+numdic[b%10]
    if a!=0:
        s+=numdic[a]+len('hundredand')
    return s
r=0
for i in range(1,1000):
    r+=lettercnt(i)
print(r+1)
"""
#p19
"""
Days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def isLeapYear(y):
    return (y%4==0 and y%100!=0) or y%400==0
def getDays(y,m,d):
    days=1
    for i in range(1900,y):
        if isLeapYear(i):
            days+=366
        else:
            days+=365
    days+=sum(Days[:m])+d
    if isLeapYear(y) and m>2:
        days+=1
    return days%7
def p19():
    cnt=0
    for y in range(1901,2001):
        for m in range(1,13):
            if getDays(y,m,1)==1:
                cnt+=1
    return cnt
print(p19())
"""
#p22
"""
letter=dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),range(1,27)))
names=[]
with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p022_names.txt', 'r') as f:
    i = 0
    while True:
        line = f.readline().strip()
        if len(line) > 1:
            i += 1
            s = list(line.split(','))
            for w in s:
                names.append(w[1:-1])
        else:
            break
names.sort()
s=0
for i in range(len(names)):
    t=0
    for w in names[i]:
        t+=letter[w]
    s+=(i+1)*t
print(s)
"""
#p26 我觉得可以猥琐一点，求出小数点后200位，找循环字串长度
"""
def getcyclen(m,n):
    l=[]
    a=m%n
    if a==0:
        return 0
    else:
        flag=False
        while True:
            a*=10
            if a%n==0:
                break
            else:
                if a//n!=0 and a//n in l:
                    flag=True
                    break
                else:
                    l.append(a//n)
                    a=a%n
        if flag:
            return len(l)-l.index(a//n)
        return 0
langest=0
n=1
for d in range(1,1000):
    if langest<getcyclen(1,d):
        n=d
        langest=getcyclen(1,d)
print(n)
"""
#27
"""
M=1000
p=primes(M)
def Quadratic_primes(a,b):
    n=1
    while isPrime(n*n+a*n+b):
        n+=1
    return n
m=0
r=0
for a in range(M):
    for b in p:
        if m<Quadratic_primes(a,b):
            m=Quadratic_primes(a,b)
            r=a*b
        if m<Quadratic_primes(-1*a,b):
            m=Quadratic_primes(-1*a,b)
            r=-1*a*b
print(r)
"""
#28
"""
s=1
for n in range(3,1002,2):
    s+=2*(2*n*n-3*(n-1))
print(s)
"""
#29
"""
N=100
##该函数返回条件范围内等于p^n的幂的个数
def equ_p_n(p,n):
    s=0
    for i in range(2,n//2+1):
        if p**i<=N:
            if n%i==0 and n//i>=2:
                s+=1
        else:
            break
    return s

pnum=primes(N)
cnt=0
for p in pnum:
    for n in range(2,N+1):
        cnt+=equ_p_n(p,n)
print((N-1)**2-cnt)
"""
#32
"""
def isPandigital(a,b,c):
    sa=str(a)
    sb=str(b)
    sc=str(c)
    if len(sa)+len(sb)+len(sc)!=9:
        return False
    else:
        l=[0 for x in range(10)]
        for d in sa:
            l[int(d)]=1
        for d in sb:
            l[int(d)]=1
        for d in sc:
            l[int(d)]=1
        if sum(l)-l[0]!=9:
            return False
        return True
p=[0 for x in range(10000)]
for i in range(1,100):
    if i<10:
        for j in range(1000,10000):
            if i*j<10000:
                if isPandigital(i,j,i*j):
                    p[i*j]=1
            else:
                break
    else:
        for j in range(100,1000):
            if i*j<10000:
                if isPandigital(i,j,i*j):
                    p[i*j]=1
            else:
                break
s=0
for i in range(10000):
    if p[i]==1:
        s+=i
print(s)
"""
#33
"""
l=[]
for i in range(11,100):
    if i%10!=0:
        a=i//10
        b=i%10
        for j in range(i+1,100):
            if j%10!=0:
                c=j//10
                d=j%10
                if a==c or a==d:
                    if b/(c+d-a)==i/j:
                        l.append((b,c+d-a))
                elif b==c or b==d:
                    if a/(c+d-b)==i/j:
                        l.append((a,c+d-b))
print(l)
"""
#38
"""
#生成全数字的排列，对于每种情况，前几个数组成n，且n最大为四位数
dig=[9,8,7,6,5,4,3,2,1]
def getnum(l,start,end):
    if end>8:
        return 0
    r=0
    while start<=end:
        r*=10
        r+=l[start]
        start+=1
    return r
def is_Pandigital_multiples(l):
    flag=False
    for p in range(1,5):
        n=getnum(l,0,p-1)
        i=2
        j=p
        while True:
            if n*i!=getnum(l,j,j+len(str(n*i))-1):
                break
            else:
                if j>8:
                    break
                j+=len(str(n*i))
                i+=1

        if j==9:
            flag=True
            break
    return flag

def p38():
    r=0
    dig = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for n in itertools.permutations(dig):
        if is_Pandigital_multiples(n):
            r=getnum(n,0,8)
            break
    return r
print(p38())
"""
#40
"""
def getDig(n):
    i=1
    m=0
    while True:
        if m+9*i*pow(10,i-1)<=n:
            m+=9*i*pow(10,i-1)
        else:
            break
        i+=1
    a=(n-m)//i
    b=(n-m)%i
    t=pow(10,i-1)+a
    if b==0:
        t-=1
        return str(t%10)
    else:
        return str(t)[b-1]


s=1
for i in range(7):
    s*=int(getDig(pow(10,i)))
print(s)
"""




