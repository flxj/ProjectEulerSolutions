def upnum(low,high,n):  #最低位大于等于low,最高位小于等于high的n位上升数的个数
    if high<low:
        return 0
    elif low==high:
        return 1
    else:
        if n<2:
            return 0
        elif n==2:
            return (high-low+2)*(high-low+1)//2
        else:
            cnt=0
            for i in range(low,high+1):
                cnt+=upnum(low,i,n//2)*upnum(i,high,n//2)
            return cnt

def downnum(low,high,n):
    if high>low:
        return 0
    elif low==high:
        return 1
    else:
        if n<2:
            return 0
        elif n==2:
            return (low-high+2)*(low-high+1)//2
        else:
            cnt=0
            for i in range(high,low+1):
                cnt+=downnum(low,i,n//2)*downnum(i,high,n//2)
            return cnt

cnt=0
for n in range(2,100):
    for i in range(10):
        for j in range(i,10):
            cnt+=(upnum(i,j,n)+downnum(j,i,n))
print(cnt)

