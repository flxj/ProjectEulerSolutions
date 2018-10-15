from math import factorial
def cni(n,i):
    return factorial(n)//factorial(i)//factorial(n-i)

def getp(n):
    return 1

maxnum=0
for i in range(3,27):
    if maxnum<cni(26,i)*(2*cni(i,2)-i+1):
        maxnum=cni(26,i)*(2*cni(i,2)-i+1)
print(maxnum)

#409511334375
#1632151300