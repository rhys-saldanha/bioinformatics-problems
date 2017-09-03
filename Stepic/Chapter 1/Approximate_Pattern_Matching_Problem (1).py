import sys

def checkDiff(a, b):
    sol = 0
    for i, j in zip(a, b):
        if i!=j:
            sol += 1
    return sol

def compare(f):
    f = open(f, 'r')
    kmer = f.readline().strip()
    k = len(kmer)

    s = ""
    while True:
        line = f.readline().strip()
        try:
            n = int(line)
            break
        except ValueError:
            s += line
            
    solutions = []
    for i in range(len(s)):
        testk = s[i:i+k]
        if len(testk) == k:
            if checkDiff(testk, kmer) <= n:
                solutions.append(i)

    for i in solutions:
        print i,

compare('dataset_8_3.txt')
            
    
    
