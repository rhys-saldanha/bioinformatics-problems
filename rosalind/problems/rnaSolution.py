def dnaRnaConvert(t):
    u = ''
    for i in t.upper():
        if i == ' ':
            pass
        elif i == 'T':
            u += 'U'
        else:
            u += i
    return u

def dnaRnaConvertDict(DNAdict):
    RNAdict = {}
    RNA = ''
    for k, i in DNAdict.items():
        for t in i.upper():
            if t == ' ':
                pass
            elif t == 'T':
                RNA += 'U'
            else:
                RNA += t
        RNAdict[k] = RNA
        RNA = ''
    return RNAdict
            
