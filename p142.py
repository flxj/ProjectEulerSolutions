import math
from eulerlib import gcd
import math
#完全勾股数字典
def getPnumAll(edgeMAX):
    res={}
    m=2
    flag=True
    while flag :
        for n in range(m-1,0,-2):
            if m*m+n*n<=edgeMAX:
                if gcd(m,n)==1:
                    t = edgeMAX // (m * m + n * n)
                    for i in range(1,t+1):
                        if (m*m+n*n)*i in res:
                            res[(m*m+n*n)*i].append((2*m*n*i,(m*m-n*n)*i))
                        else:
                            res[(m*m+n*n)*i]=[(2*m*n*i,(m*m-n*n)*i)]
            else:
                flag=False
                break
        m+=1
    return res
#基本勾股数字典
def getPnum(edgeMAX):
    res={}
    m=2
    flag=True
    while flag :
        for n in range(m-1,0,-2):
            if m*m+n*n<=edgeMAX:
                if gcd(m,n)==1:
                    if m*m+n*n in res:
                        res[m*m+n*n].append((2*m*n,m*m-n*n))
                    else:
                        res[m*m+n*n]=[(2*m*n,m*m-n*n)]
            else:
                flag=False
                break
        m+=1
    return res
#生成以a=m为一直角边的直角三角形三元组列表
def generatePythTriple(m):
    r=[]
    if m%2!=0:
        for i in range(1,m):
            if m*m%i==0:
                r.append((m,(m*m//i-i)//2,(m*m//i+i)//2))
                #r.append((m*m//i+i)//2)
        return r
    else:
        for i in range(2,m,2):
            if m*m%(2*i)==0:
                r.append((m,(m * m // i - i) // 2,(m * m // i + i) // 2))
                #r.append((m * m // i + i) // 2)
        return r

MAX=10000
dic=getPnumAll(MAX)
keys=sorted(list(dic.keys()))
xyz=[]
flag=True
i=1
while i<len(keys) and flag:
    if len(dic[keys[i]])>1:
        for j in range(0,len(dic[keys[i]])-1):
            for k in range(j+1,len(dic[keys[i]])):
                t=abs(dic[keys[i]][j][0]**2-dic[keys[i]][k][0]**2)
                t1=abs(dic[keys[i]][j][1]**2-dic[keys[i]][k][1]**2)
                t2=abs(dic[keys[i]][j][0]**2-dic[keys[i]][k][1]**2)
                t3=abs(dic[keys[i]][j][1]**2-dic[keys[i]][k][0]**2)
                if math.sqrt(t)==int(math.sqrt(t)):
                    xyz+=[keys[i], dic[keys[i]][j][0], dic[keys[i]][k][0]]
                    flag = False
                    break
                elif math.sqrt(t1)==int(math.sqrt(t1)):
                    xyz+=[keys[i], dic[keys[i]][j][1], dic[keys[i]][k][1]]
                    flag = False
                    break

                elif math.sqrt(t2)==int(math.sqrt(t2)):
                    xyz+=[keys[i], dic[keys[i]][j][0], dic[keys[i]][k][1]]
                    flag = False
                    break

                else:
                    if math.sqrt(t3)==int(math.sqrt(t3)):
                        xyz+=[keys[i], dic[keys[i]][j][1], dic[keys[i]][k][0]]
                        flag = False
                        break
    i+=1
res=0
if len(xyz)!=0:
    print(xyz)
    for i in xyz:
        res+=i*i
    print(res//2)
else:
    print("sorry")




