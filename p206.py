import math
fsum=0
for i in range(1,10):
    fsum+=i*pow(10,18-2*i)
def merge(n):
    s=0
    i=1
    while n!=0:
        d=n%10
        n//=10
        s+=d*pow(10,i)
        i+=2
    return fsum+s
for i in range(99999998,1,-2):
    if int(math.sqrt(merge(i)))==math.sqrt(merge(i)):
        print(int(math.sqrt(merge(i)))*10)
        break
