#RNA to protein

def prot(s):
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
    for i in range((len(s)/3)):
        s3.append(s[i*3:i*3+3])
    while True:
        for i in s3:
            if d[i] == '!':
                break
            else:
                l += d[i]

    return l

def protSingu(s):
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
    if len(s) == 3:
        return d[s]
    else:
        return ''
        print 'RNA Codon passed is not length 3'
        print 'Codon passed =', s
