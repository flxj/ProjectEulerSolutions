
def genMatrix(size):
    restmp=[]
    for i in range(size**2):
        k=i+1
        if k<=55:
            restmp.append((100003 - 200003*k + 300007*k*k*k) % 1000000 - 500000)
        else:
            restmp.append((restmp[-24] + restmp[-55]) % 1000000 - 500000)
    result=[restmp[i*size:(i+1)*size] for i in range(size)]
    return result
