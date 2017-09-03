def fib(file):
    f = open(file, 'r')
    n, k = f.readline().strip().split()
    n = int(n)
    k = int(k)
    a = []
    y = []
    for i in range(n):
        a.append(0)
        y.append(0)
    print n, k
    for i in range(n):
        if i == 0:
            y[i] = 1
            a[i] = 0
        else:
            a[i] = a[i-1] + y[i-1]
            y[i] = a[i-1]*k
    print a[n-1] + y[n-1]

fib('rosalind_fib.txt')
