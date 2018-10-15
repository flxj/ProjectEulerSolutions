even=[2,4,6,8]
even1=[0,2,4,6,8]
odd=[1,3,5,7,9]
def reverse(n):
    b=0
    while n>0:
        b=b*10+n%10
        n=n//10
    return b
def isOdd(n):
    while n>0:
        if n%10 in even1 :
            return False
        n=n//10
    return True

count=0
i=1
while i<pow(10,8):
    x=str(i)
    if int(x[0]) in even:
        i=(int(x[0])+1)*pow(10,len(x)-1)
    else :
        for y in even :
            n=x+str(y)
            if isOdd(int(n)+int(n[::-1])):
                count+=2
        i+=1
print(count)
