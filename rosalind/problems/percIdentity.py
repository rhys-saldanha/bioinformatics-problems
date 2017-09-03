from readFASTA import *
import collections
import sys, os

def compareSeqs(k1, s1, k2, s2, divide):
    lengths1 = 0
    lengths2 = 0
    totalLength = 0
    iden = 0
    if len(s1) != len(s2):
        print k1 + ' is not the same length as ' + k2
    else:
        for i in range(len(s1)):
            if s1[i] != '-' or s2[i] != '-':    
                if s1[i] == s2[i]:
                    iden += 1
        if divide == 's':
            for i in s1:
                if i != '-':
                    lengths1 += 1
            for i in s2:
                if i != '-':
                    lengths2 += 1
            if lengths1 < lengths2:
                totalLength = lengths1
            else:
                totalLength = lengths2

        elif divide == 'a':
            i = 0
            beginning = 'p'
            removes = 0
            while i < len(s1):
                if s1[i] != '-' or s2[i] != '-':
                    if beginning == 'p':
                        beginning = i  
                    end = i
                i += 1
            i = 0
            while i < end:
                if i > beginning:
                    if s1[i] == '-' and s1[i] == '-':
                        removes += 1
                i += 1
            totalLength = end - removes - beginning + 1

        return str(round(float(iden)/float(totalLength)*100, 2))+'%'

def percIdentity(file):
    if os.path.exists(file):
        d = readFASTA(file)
    else:
        print "usage: percIdentity.py filename"
        print "'" + file + "' not found"
        sys.exit()
    d = collections.OrderedDict(sorted(d.items()))
    percIdenList = {}
    comparedKeys = []

    while True:
        print 'Would you like to divide by the shortest sequence'
        print 'or the alignment length?'
        print '(s/a)'
        divide = raw_input().lower()
        if divide not in 'sa':
            print 'Unknown option: ' + divide
        elif divide == 'a':
            print 'Dividing by Alignment Length'
            break
        elif divide == 's':
            print 'Dividing by Shortest Sequence'
            break

    x = 0
    while x < len(d.keys()):
        k1 = sorted(d.keys())[x]
        percIdenList[k1] = {}
        y = 0
        while y <= x:
            k2 = sorted(d.keys())[y]
            percIdenList[k1][k2] = compareSeqs(k1, d[k1], k2, d[k2],divide)
            y+=1
        x+=1
    percIdenList = collections.OrderedDict(sorted(percIdenList.items()))

    for k1, v1 in percIdenList.items():
        print k1,
        for k2 in sorted(v1.keys()):
            print '\t', v1[k2],
        print
    for k1 in percIdenList.keys():
        print '\t', k1,
        
percIdentity(sys.argv[1])
