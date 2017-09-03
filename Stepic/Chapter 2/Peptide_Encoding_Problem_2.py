import sys

def protMake(s):
    d = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V', 'UUC':'F', 'CUC':'L',
         'AUC':'I', 'GUC':'V', 'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
         'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V', 'UCU':'S', 'CCU':'P',
         'ACU':'T', 'GCU':'A', 'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
         'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 'UCG':'S', 'CCG':'P',
         'ACG':'T', 'GCG':'A', 'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
         'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D', 'UAA':'!', 'CAA':'Q',
         'AAA':'K', 'GAA':'E', 'UAG':'!', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
         'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R',
         'AGC':'S', 'GGC':'G', 'UGA':'!', 'CGA':'R', 'AGA':'R', 'GGA':'G',
         'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}
    s3 = []
    l = ''
    for i in range(len(s)/3):
        s3.append(s[i*3:i*3+3])

    for codon in s3:
        if codon not in d.keys():
            break
        elif d[codon] == '!':
            break
        else:
            l += d[codon]

    return l

def revc(s):
    d = {"A":"U", "U":"A", "C":"G", "G":"C"}
    res = ""
    for i in s[::-1]:
        res += d[i]
    return res

def search(s, prot):
    results = []
    frameLen = len(prot)*3
    for i in range(len(s)):
        frame = s[i:i+frameLen]
        if len(frame) == frameLen:
            if protMake(frame) == prot or protMake(revc(frame)) == prot:
                results.append(RNAtoDNA(frame))

    for result in results:
        print result,

def DNAtoRNA(l):
    RNA = ""
    for letter in l:
        if letter == 'T':
            letter = 'U'
        RNA += letter
    
    return RNA

def RNAtoDNA(l):
    DNA = ""
    for letter in l:
        if letter == 'U':
            letter = 'T'
        DNA += letter

    return DNA

def main(f=False, prot=False, s=False):
    if f:
        f = open(f, "r")
        allFile = f.readlines()
        prot = allFile[-1].strip().upper()
        del allFile[-1]

        s = ""
        for i in allFile:
            s += i.strip().upper()

    s = DNAtoRNA(s)

    search(s, prot)

main(f="dataset_18_6.txt")
