def skew(s):
    return s.count('G')-s.count('C')
def maxskew2(s):
    m=float('-inf')
    for i in range(len(s)):
        sk=skew(s[i:])
        if sk>m:
            sol=[i]
            m=sk
        elif sk==m:
            sol.append(i)
    return sol

def maxskew(f):
    f = open(f, "r")

    s = ""
    while True:
        line = f.readline().strip()
        if not line:
            break
        s += line

    for i in maxskew2(s):
        print i,

##    Gcount = s.upper().count('G')
##    Ccount = s.upper().count('C')
##    Gcount = 0
##    Ccount = 0
##
##    l = []
##
##    for i in range(len(s)):
##        if s[i] == 'G':
##            Gcount += 1
##        if s[i] == 'C':
##            Ccount += 1
##        l.append(Gcount - Ccount)
##    
##    print l
##    d = {}
##    
##    for i in range(2,len(l)-2):
##        d[i] = False
##        x = l[i]
##        if x < l[i-2]:
##            if x < l[i-1]:
##                if x < l[i+1]:
##                    if x < l[i+2]:
##                        d[i] = True
##
##    for k, v in d.items():
##        if v:
##            print k,

maxskew('dataset_7_6.txt')
