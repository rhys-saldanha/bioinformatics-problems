import sys

def mass(p):
    d = {"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113,
         "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131,
         "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for i in p:
        ans += d[i]
    return ans

def cycloCounting(prot):
    protTemp = prot + prot
    spectrum = [0]
    
    for length in range(1,len(prot)):
        for place in range(len(prot)):
            pep = protTemp[place:place+length]
            if len(pep) == length:
                spectrum.append(mass(pep))
    spectrum.append(mass(prot))

    spectrum.sort()
    return spectrum

def counting(prot):
    protTemp = prot
    spectrum = [0]
    
    for length in range(1,len(prot)):
        for place in range(len(prot)):
            pep = protTemp[place:place+length]
            if len(pep) == length:
                spectrum.append(mass(pep))
    spectrum.append(mass(prot))

    spectrum.sort()
    return spectrum

def expand(l):
##    letters = ["G","A","S","P","V","T","C","I","L","N","D","K","Q","E","M",
##               "H","F","R","Y","W"]
    letters = ["G","A","S","P","V","T","C","I","N","D","K","E","M",
               "H","F","R","Y","W"]
    m = []
    for i in l:
        for j in letters:
            m.append(i+j)
    if not l:
        m = letters
    return m

def compareSpec(spec, pep):
    spec2 = counting(pep)
    runFull = True
    for i in spec2:
        if spec.count(i) < spec2.count(i):
            runFull = False
            break
    return runFull

def exactCompareSpec(spec, pep):
    spec2 = cycloCounting(pep)
    runFull = True
    if len(spec2) != len(spec):
        runFull = False
    for i,j in zip(spec, spec2):
        if i != j:
            runFull = False
            break
    return runFull

def sequencing(spectrum):
    allPoss = []
    correct = []
    while True:
        allPoss = expand(allPoss)
        if not allPoss:
            break
        if len(counting(allPoss[-1])) > len(spectrum):
            break
        for pep in allPoss:
            if exactCompareSpec(spectrum, pep):
                print pep
                correct.append(pep)
                allPoss.remove(pep)
            elif not compareSpec(spectrum, pep):
                allPoss.remove(pep)
    
    display(correct)
    return correct

def display(l):
    l = l[::-1]
    prints = []
    for ans in l:
        printy = ""
        for i in range(len(ans)-1):
            printy += str(mass(ans[i])) + "-"
        printy += str(mass(ans[-1]))
        print printy,
##        if printy not in prints:
##            prints.append(printy)
##    for i in prints:
##        print i,

def main(f=False, seq=False):
    if f:
        f = open(f, "r")
        seq = f.readline().strip()
    if seq:
        seq = seq.split()

    spectrum = []
    for i in seq:
        spectrum.append(int(i))
    spectrum.sort()

    sequencing(spectrum)

main(seq="0 113 128 186 241 299 314 427")
