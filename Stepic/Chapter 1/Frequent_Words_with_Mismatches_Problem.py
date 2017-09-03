import sys, itertools

combslist = ['A', 'T', 'G', 'C']

def checkDiff(a, b):
    sol = 0
    for i, j in zip(a, b):
        if i!=j:
            sol += 1
    return sol

def countKmers(l):
    print "counting kmers"
    d = {}
    highest = 0
    for kmer in l:
        if kmer in d.keys():
            d[kmer] += 1
            if d[kmer] > highest:
                highest = d[kmer]
        else:
            d[kmer] = 1

    printed = 0
    for k in sorted(d.keys()):
        v = d[k]
        if v == highest:
            print k,
            printed += 1
    print''
    print('Number printed: %s' % printed)

def compare(s, k, d):
    print "comparing"
    solutions = []
    solutionsword = ""

    for a in list(itertools.product(combslist, repeat=k)):
        kmer = ""
        for i in a:
            kmer += i
        for i in range(len(s)):
            testk = s[i:i+k]
            if len(testk) == k:
                if checkDiff(testk, kmer) <= d:
                    solutions.append(kmer)
                    solutionsword += str(kmer) + " "

    return solutionsword, solutions

def freqWordsMis(f):
    f = open(f, 'r')
    s, k, d = f.read().strip().split()
    k = int(k)
    d = int(d)

    a, b = compare(s, k, d)
    countKmers(b)


try:
    freqWordsMis(sys.argv[1])
except IndexError:
    freqWordsMis('frequent_words_mismatch_data.txt')
