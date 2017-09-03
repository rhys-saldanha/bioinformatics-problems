def fibd(file):
    f = open(file, 'r')
    n, m = f.readline().strip().split()
    #n number of months, each rabbit lives for m months
    n = int(n)
    k = 1
    m = int(m)
    a = []
    y = []
    for i in range(n):
        a.append(0)
        y.append(0)
    print n, m
    for i in range(n):
        if i == 0:
            y[i] = 1
            a[i] = 0
        elif i >= m:
            a[i] = a[i-1] + y[i-1] - y[i-m]
            y[i] = a[i-1]*k
        else:
            a[i] = a[i-1] + y[i-1]
            y[i] = a[i-1]*k
    print a[n-1] + y[n-1]

fibd('rosalind_fibd.txt')
