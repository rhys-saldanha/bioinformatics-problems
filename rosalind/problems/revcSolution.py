import sys

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

def revcRNADict(RNADict):
    RNARevDict = {}
    for k, s in RNADict.items():
        s = s[::-1].upper()
        l = ''
        for i in s:
            if i == 'A':
                l += 'U'
            elif i == 'U':
                l += 'A'
            elif i == 'C':
                l += 'G'
            elif i == 'G':
                l += 'C'
        RNARevDict[k + '_reversed'] = l
    return RNARevDict

def revcFile(n):
    s = open(n, 'r').read().strip()
    revc(s)

        
        
