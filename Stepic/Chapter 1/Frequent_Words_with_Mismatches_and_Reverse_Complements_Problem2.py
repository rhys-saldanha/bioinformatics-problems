import sys, operator
from itertools import combinations, product

def generate(s, d=2):
    N = len(s)
    letters = 'ACGT'
    pool = list(s)

    for indices in combinations(range(N), d):
        for replacements in product(letters, repeat=d):
            skip = False
            for i, a in zip(indices, replacements):
                if pool[i] == a:
                    skip = True
            if skip: continue

            keys = dict(zip(indices, replacements))
            yield ''.join([pool[i] if i not in indices else keys[i] 
                           for i in range(N)])


def allGenerate(kmers, d):
    mis = {}
    for i in kmers.keys():
        mis[i] = (list(generate(i))).append(i)
    return mis


def findKmers(s, k):
    result = {}
    for i in range(len(s)):
        if len(s[i:i+k]) == k:
            result[s[i:i+k]] = 0
    return result


def findReverse(d):
    k = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev = {}
    for i in d.keys():
        sol = ""
        for j in i[::-1]:
            sol += k[j]
        rev[sol] = 0
    return rev

def revc(s):
    s = s[::-1].upper()
    k = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} 
    l = ''
    for i in s:
        l += k[i]
    return l

def counter(s, kmers, countedkmers):
    for kmer in kmers.keys():
        for subKmer in kmer:
            countedkmers[kmer] = sum(s[i:i+len(subKmer)] == subKmer
                                for i in xrange(len(s)-len(subKmer)+1))
    return countedkmers

def disHighest(kmers):
    highest = kmers[max(kmers.iteritems(), key=operator.itemgetter(1))[0]]
    for k in sorted(kmers.keys()):
        try:
            v = kmers[k]
            a = kmers[revc(k)]
        except KeyError:
            try:
                v = kmers[k]
                a = 0
            except KeyError:
                v = -1
                a = -1

        if v + a >= highest:
            print k, revc(k)

def main(f):
    f = open(f, 'r')
    s, k, d = f.read().strip().split()
    k = int(k)
    d = int(d)

    kmers = findKmers(s, k)
    kmers.update(findReverse(kmers))
    kmers = allGenerate(kmers, d)
    
    countedkmers = {}
    for kmer in kmers.keys():
        countedkmers[kmer] = 0
    countedkmers = counter(s, kmers, countedkmers)

    print countedkmers
    disHighest(countedkmers)
    global kmers

main('frequent_words_mismatch_data.txt')
    

