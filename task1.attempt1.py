def formula(ni,a,b):
    n2 = ni*a-(ni*ni)*b
    return n2
def run(ni,a,b):
    numlist=[]
    ndif= 1000
    counter = 0
    while ndif >= 0.00005:
        n2=formula(ni,a,b)
        if n2 < 0.0001:
            n2 = 0
            break
        ndif=(n2/ni)
        ndif=abs(ndif - 1)
        ni=n2
        counter= counter+1
        if b == 0:
            n2=-1
            break
    return n2

with open("tests.txt") as f:
    for line in f:
        line = line.split(" ")
        n = run(ni=float(line[0]),a=float(line[1]),b=float(line[2]))
        print(n)
