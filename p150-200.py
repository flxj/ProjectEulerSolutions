import math
import eulerlib
from time import  time
from queue import Queue
#p171


#p181
"""
##当只有一种颜色时的分堆
def fone(n):
    if n<=1:
        return 1
    s=2
    for i in range(2,n):
        s+=pow(i,n-i)//i
    return s
##当两种颜色混在一起时的分堆，此时分成的每堆两色至少各有一个
def ftwo(m,n):
    if m*n==0:
        if m==0 and n==0:
            return 1
        else:
            return 0
    if m==1 or n==1:
        return 1
    p=min(m,n)
    s=2
    for i in range(2,p):
        s+=pow(i,m-i)*pow(i,n-i)//i
    return s

def getGroup(m,n):
    r=0
    for b in range(m+1):
        for w in range(n+1):
            r+=fone(m-b)*fone(n-w)*ftwo(b,w)
    return r
print(getGroup(3,2))
print(ftwo(3,3))

##83735848679360680
"""
#183
"""
start=time()
N=10000
def is_terminating_decimal2(n,k):
    num = n
    gcd = eulerlib.gcd(num,k)
    while gcd != 1:
        num = num //gcd
        k = k //gcd
        gcd = eulerlib.gcd(num, k)
    while k % 2 == 0:
        k//=2
    while k % 5 == 0:
        k//=5
    if k == 1:  # P terminates
        return True
    else:
        return False
res=0
for i in range(5,N+1):
    if is_terminating_decimal2(i,round(i/2.71828)):
        res-=i
    else:
        res+=i
print(res)
print((time()-start)*1000)
"""
#p172

#p191
"""
D=5
f=[[0,0,0] for i in range(D+1)]
f[1][0],f[2][0],f[3][0]=1,2,4
for i in range(4,D+1):
    f[i][0]=pow(2,i-1)-(i-3)*pow(2,i-4)
f[1][1],f[1][2]=1,1
for i in range(2,D+1):
    f[i][1]=f[i-1][0]+f[i-1][1]+f[i-1][2]
    f[i][2]=f[i-1][0]+f[i-1][1]+f[i-1][2]-f[i-2][2]
print(f[4][0],f[4][1],f[4][2])
#print(f[D][0]+f[D][1]+f[D][2])
"""
#p215
#806844323190414
"""
M,N=32,10
f=[0 for i in range(M+1)]
f[2],f[3]=1,1
for i in range(4,M+1):
    f[i]=f[i-2]+f[i-3]
print(f[M])
"""
#186
"""
class Call(object):
    def __init__(self):
        self.Sk24=Queue(24)
        self.Sk55=Queue(55)
    def called(self,k):
        Sk=0
        if k<=55 and k>=1:
            Sk=(100003-200003*k+300007*k*k*k)%1000000
        else:
            Sk=(self.Sk55.get()+self.Sk24.get())%1000000
        if k>=32:
            self.Sk24.put(Sk)
        self.Sk55.put(Sk)
        return Sk
def p186():
    pm=524287
    friends={}
    friends[pm]=set()

    n=0
    pmfriends = len(friends[pm])
    call=Call()

    while pmfriends+1<990000:
        n+=1
        caller=call.called(2*n-1)
        called=call.called(2*n)
        if caller!=called:
            if caller==pm:
                if called in friends:
                    friends[pm] = friends[pm] | friends[called]
                friends[pm].add(called)
            elif called==pm:
                if caller in friends:
                    friends[pm] = friends[pm] | friends[caller]
                friends[pm].add(caller)
            else:
                if caller not in friends[pm] and called not in friends[pm]:
                    if caller not in friends:
                        friends[caller]=set()
                    if called not in friends:
                        friends[called]=set()
                    friends[caller].add(called)
                    friends[called].add(caller)

                else:
                    if caller in friends[pm]:
                        if called in friends:
                            friends[pm]=friends[pm] | friends[called]
                        friends[pm].add(called)

                    if called in friends[pm]:
                        if caller in friends:
                            friends[pm] = friends[pm] | friends[caller]
                        friends[pm].add(caller)
        pmfriends=len(friends[pm])
    return n
print(p186())
"""
"""
def euler186():
    l = [(300007 * i ** 3 - 200003 * i + 100003) % 1000000 for i in range(1, 56)]
    fr = [[i] for i in range(1000000)]
    calls = k = v = 0

    while len(fr[524287]) < 990000:
        for i in range(2):
            u, v, l[k], k = v, l[k], (l[k] + l[k - 24]) % 1000000, (k + 1) % 55

        if u != v:
            calls += 1
            ufr, vfr = fr[u], fr[v]

            if ufr is not vfr:
                if len(ufr) < len(vfr):
                    ufr, vfr = vfr, ufr
                ufr.extend(vfr)
                for i in vfr:
                    fr[i] = ufr
    return calls
print(euler186())
"""
#165
"""
#判断线段是否相交
class segments_insert(object):
    def direction(self,pix,piy,pjx,pjy,pkx,pky):
        return (pjx-pix)*(pky-piy)-(pkx-pix)*(pjy-piy)
    def on_segment(self,pix,piy,pjx,pjy,pkx,pky):
        if min(pix,pjx)<=pkx and pkx<=max(pix,pjx) and min(piy,pjy)<=pky and pky<=max(piy,pjy):
            return True
        return False
    def insert(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
        d1=self.direction(p3x,p3y,p4x,p4y,p1x,p1y)
        d2=self.direction(p3x,p3y,p4x,p4y,p2x,p2y)
        d3=self.direction(p1x,p1y,p2x,p2y,p3x,p3y)
        d4=self.direction(p1x,p1y,p2x,p2y,p4x,p4y)

        if ((d1>0 and d2<0) or (d1<0 and d2>0)) and ((d3>0 and d4<0) or ( d3<0 and d4>0)):
            return True
        elif d1==0 and self.on_segment(p3x,p3y,p4x,p4y,p1x,p1y):
            return True
        elif d2==0 and self.on_segment(p3x,p3y,p4x,p4y,p2x,p2y):
            return True
        elif d3==0 and self.on_segment(p1x,p1y,p2x,p2y,p3x,p3y):
            return True
        elif d4==0 and self.on_segment(p1x,p1y,p2x,p2y,p4x,p4y):
            return True
        else:
            return False
    #只关注真焦点
    def insert2(self, p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y):
            d1 = self.direction(p3x, p3y, p4x, p4y, p1x, p1y)
            d2 = self.direction(p3x, p3y, p4x, p4y, p2x, p2y)
            d3 = self.direction(p1x, p1y, p2x, p2y, p3x, p3y)
            d4 = self.direction(p1x, p1y, p2x, p2y, p4x, p4y)

            if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
                return True
            return False
def p165():
    segments=[]
    s=290797
    for i in range(1,20000):
        segments.append(s%500)
        s=s**2%50515093
    res=0
    inst=segments_insert()
    for i in range(4,len(segments),4):
        for j in range(i+4,len(segments),4):
            if inst.insert2(segments[i-3],segments[i-2],segments[i-1],segments[i],segments[j-3],segments[j-2],segments[j-1],segments[j]):
                res+=1
    print(res)
p165()
"""
#2866639
#2868868
#
#p345
"""
import PElib


def compute():
    # Memoization
    maxsum = [[None] * (2 ** COLUMNS) for _ in range(ROWS)]

    # Returns the maximum sum when considering the submatrix from row 'startrow' until the bottom,
    # with the bit set 'setofcols' indicating which column indexes are still free to be used.
    def find_maximum_sum(startrow, setofcols):
        if startrow == ROWS:
            assert PElib.popcount(setofcols) == COLUMNS - ROWS
            return 0
        if maxsum[startrow][setofcols] is None:
            result = 0
            col = 0
            bit = 1
            while True:
                if bit > setofcols:
                    break
                if setofcols & bit != 0:
                    result = max(MATRIX[startrow][col] + find_maximum_sum(startrow + 1, setofcols ^ bit), result)
                col += 1
                bit <<= 1
            maxsum[startrow][setofcols] = result
        return maxsum[startrow][setofcols]

    ans = find_maximum_sum(0, 2 ** COLUMNS - 1)
    return str(ans)


MATRIX = (
    (7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583),
    (627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913),
    (447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743),
    (217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350),
    (960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350),
    (870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803),
    (973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326),
    (322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973),
    (445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848),
    (414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198),
    (184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390),
    (821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574),
    (34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699),
    (815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107),
    (813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805),
)

ROWS = len(MATRIX)
COLUMNS = len(MATRIX[0])
print(compute())
"""
#197
"""
from math import  floor
def f(x):
    return floor(2.0**(30.403243784 - x * x))/1.0e9
M=10**12
x=-1.0
y=-1.0
i=0
while i<M:
    if i>0 and x==y:
        break
    x=f(x)
    y=f(f(y))
    i+=1
r=(M-i)%i
for i in range(r):
    x=f(x)
res=floor((x+f(x))*1.0e9)/1.0e9
print("{:.9f}".format(res))
"""
#217
from eulerlib import is_prime
from math import  sqrt




























