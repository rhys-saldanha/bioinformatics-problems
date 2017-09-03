import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def lia(file):
    f = open(file, 'r')
    k, N = f.readline().strip().split()
    f.close()
    pop_k = 2**k
    print(nCr(pop_k, N) * (0.25**N) * (0.75**(pop_k-N)))

lia('rosalind_lia.txt')
