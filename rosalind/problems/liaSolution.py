import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def lia(file):
    f = open(file, 'r')
    k, N = f.readline().strip().split()
    f.close()
    k = int(k)
    N = int(N)
    pop_k = 2**k
    ans = 0
    while N < pop_k+1:
    	ans += nCr(pop_k, N) * (0.25**N) * (0.75**(pop_k-N))
    	N+=1
    print("%.3f" % ans)

lia('rosalind_lia.txt')
