def hamm(file):
    f = open(file, 'r')
    s = f.readline().strip().upper()
    t = f.readline().strip().upper()
    hammdist = 0
    if len(s) != len(t):
        print 'DNA strings do not have the same length!'
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                hammdist += 1

    print 'Hamming distance = ', hammdist

hamm('rosalind_hamm.txt')
