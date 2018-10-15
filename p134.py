
import eulerlib, itertools


primes = eulerlib.primes(1000000)
primes=primes[2:]
s=0
for i in range(len(primes)-1):
    j=i+1
    x=1
    while True:
        n=x*pow(10,len(str(primes[i])))+primes[i]
        if n%primes[j]==0:
            s+=n
            #print(n)
            break
        x+=1
print(s)

"""
def compute():
	ans = 0
	primes = eulerlib.primes(2000000)
	for i in itertools.count(2):
		p = primes[i]
		q = primes[i + 1]
		if p > 1000000:
			break
		k = 1
		while k < p:
			k *= 10
		m = (q - p) * eulerlib.reciprocal_mod(k % q, q) % q
		ans += m * k + p
	return str(ans)


if __name__ == "__main__":
    print(compute())
"""