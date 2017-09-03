from revcSolution import revcRNADict
from rnaSolution import dnaRnaConvertDict
from protSolution import protSingu
from readFASTA import *

def orf(file):
    DNAStrings = readFASTA(file)#convert FASTA file to DNA dict
    RNAStrings = dnaRnaConvertDict(DNAStrings)#convert DNAs to RNAs
    RNARevStrings = revcRNADict(RNAStrings)#create reverse-complement RNAs
    
    CodonStrings = {}#beginning of codons creation
    for k, s in RNAStrings.items():
        CodonStrings[k] = ['','','']#for any given DNA/RNA string 'k', there are 3 reading frames
        for i in range(len(s)):
            prot = protSingu(s[i:i+3])
            CodonStrings[k][i%3] += prot

    for k, s in RNARevStrings.items():
        CodonStrings[k] = ['','','']
        for i in range(len(s)):
            prot = protSingu(s[i:i+3])
            CodonStrings[k][i%3] += prot

    ProtStrings = {}
    CleanProtStrings = []
    for k, l in CodonStrings.items():
        ProtStrings[k] = [[],[],[]]
        for CodonString in range(len(l)):
            for i in range(len(l[CodonString])):
                if l[CodonString][i] == 'M':
                    p = i
                    ProtString = ''
                    while True:
                        if p >= len(l[CodonString]):
                            ProtString = False
                            break
                        elif l[CodonString][p] == '!':
                            break
                        else:
                            ProtString += l[CodonString][p]
                        p += 1
                    if ProtString:
                        if ProtString not in CleanProtStrings:
                            CleanProtStrings.append(ProtString)
                            ProtStrings[k][CodonString].append(ProtString)

    for k, l in ProtStrings.items():
        for i in (0,1,2):
            for s in l[i]:
                if s != '':
                    print s
        
print('Input name of FASTA file')
file = raw_input()

orf(file)
        
                
