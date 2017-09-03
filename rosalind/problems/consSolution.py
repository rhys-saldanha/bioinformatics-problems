#find the consensus string of multiple DNA strings

def cons(file):
    f = open(file, 'r')
    d = {}
    while True:
        p = f.read(1)
        if p == '>':
            i = f.readline().strip()
            v = f.readline().strip()
            d[i] = v
        elif not p:
            break
        elif p in 'ATCG':
            p += f.readline().strip()
            d[i] += p

    s, x = d.items()[0]
    end = len(x)
    A = []
    C = []
    G = []
    T = []
    answer = ''
    for i in range(end):
        A.append(0)
        C.append(0)
        G.append(0)
        T.append(0)

    for i in range(end):
        for k, p in d.items():
            p = p[i].upper()
            if p == 'A':
                A[i] += 1
            if p == 'C':
                C[i] += 1
            if p == 'G':
                G[i] += 1
            if p == 'T':
                T[i] += 1
        k = A[i]
        l = 'A'
        if k < C[i]:
            k = C[i]
            l = 'C'
        if k < G[i]:
            k = G[i]
            l = 'G'
        if k < T[i]:
            k = T[i]
            l = 'T'
        answer += l

    print answer
    for l in 'ACGT':
        print(l + ':'),
        for i in range(end):
            if l == 'A':
                print(A[i]),
            if l == 'C':
                print(C[i]),
            if l == 'G':
                print(G[i]),
            if l == 'T':
                print(T[i]),
        print''
        
cons('rosalind_cons.txt')
