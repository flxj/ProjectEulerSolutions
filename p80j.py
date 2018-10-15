MAX=100000000

a=[]
n=80
with open('C:/Users/George.Liu/PycharmProjects/project_euler_solution/p82.txt','r') as f:
    while True:
        line=f.readline().strip()
        if len(line)>1:
            s=list(line.split(','))
            l=[]
            for i in s:
                l.append(int(i))
            a.append(l)
        else:
            break
up_right=[0 for i in range(n)]
down_right=[0 for i in range(n)]
for j in range(1,n):
    up_right[n-1]=a[n-1][j]+a[n-1][j-1]
    down_right[0]=a[0][j]+a[0][j-1]
    for i in range(1,n):
        down_right[i]=min(down_right[i-1],a[i][j-1])+a[i][j]
        up_right[n-i-1]=min(up_right[n-i],a[i][j-1])+a[i][j]
    for i in range(n):
        a[i][j]=min(down_right[i],up_right[i])
minp=MAX
for i in range(n):
    if a[i][n-1]<minp:
        minp=a[i][n-1]
print(minp)
