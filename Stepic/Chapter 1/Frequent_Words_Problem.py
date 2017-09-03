import sys, collections

def freqWordsProb(n):
    while True:
        if n[-4:] == '.txt':
            f = open(n, 'r')
        else:
            print('File passed: ' + n)
            print(n + ' is not a txt file. Please append .txt')
            break

        s = ''
        while True:
            line = f.readline().strip()
            try:
                k = int(line)
                break
            except ValueError:
                s += line
            
            
        d = {}
        highest = 0

        for i in range(len(s)):
            kmer = s[i:i+k]
            if len(kmer) == k:
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
        break

try:
    freqWordsProb(sys.argv[1])
except IndexError:
    print('Please type in file name')
    freqWordsProb(raw_input())
    
