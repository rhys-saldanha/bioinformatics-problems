def readFASTA(file):
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
        else:
            p += f.readline().strip()
            d[i] += p
    return d
