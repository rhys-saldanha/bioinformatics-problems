def skew(f):
    f = open(f, "r")

    s = ""
    while True:
        line = f.readline().strip()
        if not line:
            break
        s += line

    #Gcount = s.upper().count('G')
    #Ccount = s.upper().count('C')
    Gcount = 0
    Ccount = 0

    l = []

    for i in range(len(s)):
        if s[i] == 'G':
            Gcount += 1
        if s[i] == 'C':
            Ccount += 1
        l.append(Gcount - Ccount)

    print l
    d = {}
    
    for i in range(2,len(l)-2):
        d[i] = False
##        for x in l[i-2:i+2]:
##            if l[i] > x:
##                d[i] = False
        x = l[i]
        if x < l[i-2]:
            if x < l[i-1]:
                if x < l[i+1]:
                    if x < l[i+2]:
                        d[i] = True

    for k, v in d.items():
        if v:
            print k,

skew('minimum_skew_data.txt')
