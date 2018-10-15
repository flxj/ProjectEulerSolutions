def div7(n,k):
    if n//7-(n-k)//7>k//7:
        return True
    else:
        return False
"""
s=0
top=101
for n in range(7,top):
    count=0
    for k in range(1,n//2):
        if div7(n,k):
            count+=2
    if n%2==0:
        if div7(n,n//2):
            count+=1
    else:
        if div7(n,n//2):
            count+=2
    s+=count
    print(count)
print(s)
#print(count)
#print(5050-count)
"""

import eulerlib, fractions
import math


def compute():
    LIMIT = 100000000

    # Pythagorean triples theorem:
    #   Every primitive Pythagorean triple with a odd and b even can be expressed as
    #   a = st, b = (s^2-t^2)/2, c = (s^2+t^2)/2, where s > t > 0 are coprime odd integers.
    ans = 0
    for s in range(3, int(math.sqrt(LIMIT * 2)), 2):
        for t in range(1, s, 2):
            a = s * t
            b = (s * s - t * t) // 2
            c = (s * s + t * t) // 2
            p = a + b + c
            if p >= LIMIT:
                break
            if c % (a - b) == 0 and fractions.gcd(s, t) == 1:
                ans += (LIMIT - 1) // p
    return str(ans)


if __name__ == "__main__":
    print(compute())