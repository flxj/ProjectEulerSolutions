import eulerlib
primes=eulerlib.primes(1000)
def d(n,p):
    count=0
    if n<p:
        if n==0:
            return 1
        else:
            return 0
    elif n==p:
        return 1
    else:
        for i in range(primes.index(p)+1):
            count+=d(n-p,primes[i])
        return count

def p(n):
    count=0
    index=0
    while n>primes[index]:
        count+=d(n,primes[index])
        index+=1
    return count


i=5
while p(i)<5000:
    i+=1
print(i)
