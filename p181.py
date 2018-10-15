from sympy import npartitions
def separate(n,t):
    ways=0
    if n<t:
        return 0
    if t==1 or t==n:
        return 1
    else:
        for i in range(1,t+1):
            ways+=separate(n-t,i)
        return ways
def p(n):
    if n==0:
        return 1
    else:
        c=0
        for i in range(1,n+1):
            c+=separate(n,i)
        return c

def solution(b,w):
    plist = [p(n) for n in range(b+1)]
    count = 0
    for i in range(1, b+1):
        for j in range(1, w+1):
            count += npartitions(b-i)*npartitions(w-j)
    print(count + npartitions(b) * npartitions(w))

solution(60,40)






