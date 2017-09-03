import sys, operator
from itertools import combinations, product

def generate(s, d=2):
    N = len(s)
    letters = 'ACGT'
    pool = list(s)

    for indices in combinations(range(N), d):
        for replacements in product(letters, repeat=d):
            keys = dict(zip(indices, replacements))
            yield ''.join([pool[i] if i not in indices else keys[i] 
                           for i in range(N)])

def allGenerate(kmers, d):
    mis = {}
    for i in kmers.keys():
        mis[i] = (list(generate(i))).append(i)
    return mis

def checkDiff(a, b, d):
    sol = 0
    for i, j in zip(a, b):
        if i!=j:
            sol += 1
    if sol <= d:
        return True
    else:
        return False

def main(f=False, k=False, d=False, s=False):
    s_all = s.strip().split()
    if f:
        f = open(f, "r")
        k, d = f.readline().strip()
        s_all = f.readlines()

    kmers = []
    for s in s_all:
        for i in range(len(s)):
            kmer = s[i:i+k]
            if len(kmer) == k:
                kmers.append(kmer)
    print kmers
    
    solutions = []
    for kmer in kmers:
        for d_kmer in list(generate(kmer,d)):
            for k_slice in kmers:
                if checkDiff(k_slice, d_kmer, d):
                    if k_slice not in solutions:
                        solutions.append(k_slice)
    for i in solutions:
        print i,
                
main(k=5, d=2, s="""TCTGAGCTTGCGTTATTTTTAGACC
GTTTGACGGGAACCCGACGCCTATA
TTTTAGATTTCCTCAGTCCACTATA
CTTACAATTTCGTTATTTATCTAAT
CAGTAGGAATAGCCACTTTGTTGTA
AAATCCATTAAGGAAAGACGACCGT""")
