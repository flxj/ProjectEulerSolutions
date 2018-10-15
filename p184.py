import math

def countpoints(xa,ya,xb,yb,n):
    count=0
    if xa*xb==0:
        if xa==xb:
            return 0
        else:
            if xa==0:
                sign=-1*int(xb/abs(xb))
                for i in range(1,n+1):
                    count=count+n+sign*int(yb*i/xb)
            else:
                sign = -1 * int(xa / abs(xa))
                for i in range(1, n + 1):
                    count = count+n+sign * int(ya * i / xa)
            return count
    elif xa*xb>0:
        if xa>0:
            if ya/xa==yb/xb:
                return 0
            else:
                if ya / xa < yb / xb:
                    xa, xb = xb, xa
                    ya, yb = yb, ya
                for i in range(-n, 0):
                    count = count + int(yb * i / xb) - int(ya * i / xa)
                return count
        else:
            if ya/xa==yb/xb:
                return 0
            else:
                if ya / xa > yb / xb:
                    xa, xb = xb, xa
                    ya, yb = yb, ya
                for i in range(1, n):
                    count = count + int(yb * i / xb) - int(ya * i / xa)
                return count
    else:
        count = n
        if xa>0:
            for i in range(-n,0):
                count=count+2*n+int(ya*i/xa)+int(yb*(n+i+1)/xb)
        else:
            for i in range(-n,0):
                count=count+2*n+int(yb*i/xb)+int(ya*(n+i+1)/xa)
        return count

def triangles(n):
    count=0
    for ya in range(n,0,-1):
        for xa in range(0,n+1):
            t=xa
            for yb in range(ya,-1,-1):
                while t<n+1:
                    xb=t%(n+1)
                    count=count+countpoints(xa,ya,xb,yb,n)+countpoints(-1*xa,ya,xb,yb,n)\
                          +countpoints(xa,ya,-1*xb,yb,n)+countpoints(-1*xa,ya,-1*xb,yb,n)
                    t+=1
    return 2*count

#r=105//math.sqrt(2)

print(triangles(1))
