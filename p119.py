import itertools
"""
dic=dict(zip([x for x in range(10)],[[] for i in range(10)]))
for i in range(10):
    d=i*i%10
    while 1:
        if d in dic[i]:
            break
        else:
            dic[i].append(d)
            d=d*i%10
def digsum(n):
    s=0
    while n!=0:
        s+=n%10
        n=n//10
    return s
cnt=10
x=614657
while cnt<30:
    n=digsum(x)
    if x%10 not in dic[n%10]:
        x+=1
    else:
        flag=False
        y=dic[n%10].index(x%10)+2
        m=pow(n,y)
        while m<=x:
            if m==x:
                flag=True
                break
            else:
                m=m*pow(n,len(dic[n%10]))
        if flag:
            cnt+=1
        x+=1
print(x-1)
"""
def compute():
    INDEX = 30  # 1-based
    limit = 1
    while True:
        candidates = set()
        k = 2
        while (1 << k) < limit:
            for n in itertools.count(2):
                pow = n**k
                if pow >= limit and len(str(pow)) * 9 < n:
                    break
                if pow >= 10 and is_digit_sum_power(pow):
                    candidates.add(pow)
            k += 1
        if len(candidates) >= INDEX:
            return str(sorted(candidates)[INDEX - 1])
        limit <<= 8


def is_digit_sum_power(x):
    digitsum = sum(int(c) for c in str(x))
    if digitsum == 1:# Powers of 10 are never a power of 1
        return False
    pow = digitsum
    while pow < x:
        pow *= digitsum
    return pow == x


if __name__ == "__main__":
    print(compute())

