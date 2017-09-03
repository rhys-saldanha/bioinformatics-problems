def ACGTcount(file):
    f = open(file, 'r')
    string = f.read()
    l = [0,0,0,0]
    for i in string.upper():
        if i == 'A':
            l[0] += 1
        elif i == 'C':
            l[1] += 1
        elif i == 'G':
            l[2] += 1
        elif i == 'T':
            l[3] += 1
        else:
            print i + ' not recognised'
    print l[0], l[1], l[2], l[3]
