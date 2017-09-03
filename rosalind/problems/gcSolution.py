def gcCalc(s):
    CTin = 0
    for i in s:
        if i.upper() in 'CG':
            CTin += 1
    return float(CTin) / float(len(s)) * 100

def gcSolution(file):
    f = open(file, 'r')
    d = {}
    n = {'X':0.0}
    highest = 'X'
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

    for i,v in d.items():
        n[i] = gcCalc(v)
        
    for i,v in n.items():
        if v > n[highest]:
            highest = i

    print highest
    print n[highest]

gcSolution('rosalind_gc.txt')
