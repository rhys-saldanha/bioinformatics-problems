import sys, itertools, operator

combslist = ['A', 'T', 'G', 'C']

def revc(s):
    s = s[::-1].upper()
    l = ''
    for i in s:
        if i == 'A':
            l += 'T'
        elif i == 'T':
            l += 'A'
        elif i == 'C':
            l += 'G'
        elif i == 'G':
            l += 'C'
    return l

def checkDiff(a, b):
    sol = 0
    for i, j in zip(a, b):
        if i!=j:
            sol += 1
    return sol

def compare(s, k, d):
    print "Comparing and counting"
    solutions = []
    solutionsword = ""

    dic = {}
    highest = 0
    
    kmers = []
    for a in list(itertools.product(combslist, repeat=k)):
        kmer = ""
        for i in a:
            kmer += i
        kmers.append(kmer)
    
    zeros = []
    for i in range(len(kmers)):
        zeros.append(0)
    allPossKmers = dict(itertools.izip(kmers, zeros))

    print "Testing"
    for i in range(len(s)):
        testk = s[i:i+k]
        if len(testk) == k:
            for kmer in allPossKmers:
                if checkDiff(testk, kmer) <= d:
                    if kmer in dic.keys():
                        dic[kmer] += 1
                    elif revc(kmer) in dic.keys():
                        dic[revc(kmer)] += 1
                    else:
                        dic[kmer] = 1

    highest = dic[max(dic.iteritems(), key=operator.itemgetter(1))[0]]
    print "Highest: %s" % highest
    for k in sorted(dic.keys()):
        try:
            v = dic[k]
            a = dic[revc(k)]
        except KeyError:
            try:
                v = dic[k]
                a = 0
            except KeyError:
                v = -1
                a = -1

        if v + a == highest:
            print k, revc(k)
    return dic

def freqWordsMis(f):
    f = open(f, 'r')
    s, k, d = f.read().strip().split()
    k = int(k)
    d = int(d)

    return compare(s, k, d)

try:
    freqWordsMis(sys.argv[1])
except IndexError:
    dic = freqWordsMis('dataset_8_5.txt')
