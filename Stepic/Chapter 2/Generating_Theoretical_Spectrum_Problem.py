import sys

def mass(p):
    d = {"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "I":113,
         "L":113, "N":114, "D":115, "K":128, "Q":128, "E":129, "M":131,
         "H":137, "F":147, "R":156, "Y":163, "W":186}
    ans = 0
    for i in p:
        ans += d[i]
    return ans

def counting(prot):
    protTemp = prot + prot
    spectrum = [0]
    
    for length in range(1,len(prot)):
        for place in range(len(prot)):
            pep = protTemp[place:place+length]
            if len(pep) == length:
                print pep
                spectrum.append(mass(pep))
    spectrum.append(mass(prot))

    spectrum.sort()
    return spectrum

def main(f=False, prot=False):
    if f:
        f = open(f, "r")
        prot = f.readline().strip().upper()

    for i in counting(prot):
        print i,

main(f="dataset_20_3.txt")
