import sys

def clumpFindFile(f):
    f = open(f, 'r')
    s = ""
    while True:
        line = f.readline().strip()
        if not line:
            break
        try:
            k, L, t = line.split()
            k = int(k)
            L = int(L)
            t = int(t)
        except ValueError:
            s += line

    print k, L, t

    LtClump = []

    for i in range(len(s)):
        clump = s[i:i+L]
        kmers = {}
        if len(clump) == L:
            for x in range(L):
                kmer = clump[x:x+k]
                if len(kmer) == k:
                    if kmer in kmers.keys():
                        kmers[kmer] += 1
                    else:
                        kmers[kmer] = 1
                    if kmers[kmer] >= t:
                        if kmer not in LtClump:
                            LtClump.append(kmer)

    for i in LtClump:
        print i,
            
        

try:
    clumpFindFile(sys.argv[2])
except IndexError:
    clumpFindFile(raw_input("Please input name of file: "))
