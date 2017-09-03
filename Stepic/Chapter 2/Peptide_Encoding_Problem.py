##from Protein_Translation_Problem import *
import sys, itertools

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
codons ={'A': ['GCG', 'GCA', 'GCC', 'GCU'],
         '!': ['UAA', 'UGA', 'UAG'],
         'C': ['UGU', 'UGC'],
         'E': ['GAA', 'GAG'],
         'D': ['GAU', 'GAC'],
         'G': ['GGU', 'GGG', 'GGA', 'GGC'],
         'F': ['UUU', 'UUC'],
         'I': ['AUC', 'AUA', 'AUU'],
         'H': ['CAU', 'CAC'],
         'K': ['AAA', 'AAG'],
         'M': ['AUG'],
         'L': ['CUU', 'CUG', 'CUA', 'CUC', 'UUG', 'UUA'],
         'N': ['AAC', 'AAU'],
         'Q': ['CAG', 'CAA'],
         'P': ['CCU', 'CCG', 'CCA', 'CCC'],
         'S': ['AGC', 'AGU', 'UCU', 'UCG', 'UCC', 'UCA'],
         'R': ['CGG', 'AGG', 'AGA', 'CGU', 'CGA', 'CGC'],
         'T': ['ACC', 'ACU', 'ACG', 'ACA'],
         'W': ['UGG'],
         'V': ['GUC', 'GUA', 'GUG', 'GUU'],
         'Y': ['UAU', 'UAC']}

def generate(protein):
    pool = []
    for i in protein:
        for j in range(len(codons[i])):
            pool.append((i,j))
    return   itertools.combinations(pool, r=len(protein))

def links(protein, pool):
    good_links = []
    for link in pool:
        poss_link = 0
        for i in range(len(protein)):
            if protein[i] == link [i][0]:
                poss_link += 1
        if poss_link == len(protein):
            good_links.append(link)
    return good_links
                
def produceRNA(links):
    RNAs = []
    for link in links:
        RNA = ""
        for i in range(len(link)):
            RNA += codons[link[i][0]][link[i][1]]
        RNAs.append(RNA)
    return RNAs

def revc(s):
    d = {"A":"T", "T":"A", "C":"G", "G":"C"}
    res = ""
    for i in s[::-1]:
        res += d[i]
    return res

def RNAtoDNA(l):
    DNAs = []
    for i in l:
        DNA = ""
        for letter in i:
            if letter == 'U':
                letter = 'T'
            DNA += letter
        DNAs.append(DNA)
    
    return DNAs

def search(s, DNAs):
    found = []
    for DNA in DNAs:
        if DNA in s:
            found.append(DNA)
            print DNA
        if revc(DNA) in s:
            found.append(revc(DNA))
            print revc(DNA)
    return found

def main(f=False, prot=False, s=False):
    if not prot and not s:
        f = open(f,"r")
        allFile = f.readlines()
        prot = allFile[-1].strip().upper()
        del allFile[-1]

        s = ""
        for i in allFile:
            s += i.strip().uper()

    return search(s, RNAtoDNA(produceRNA(links(prot, list(generate(prot))))))

#found = main(prot = "KEVFEPHYY".strip(), s = "TTCGAATCCGTATTGCTTTGGTTGGTTGAGAGAGCGACCTACATTGCTAGTCAGAATAGGTGATTCACACAAAGCTTAGCACCTGGGCAGCACCCCGTGATGTAAACCTATGGGAACTAAGGGAGTCCTGCGGTTTTAGCCAGCAAGCGAGCCGGCAGGAACACTCATACCATCGGACGCGTTTGACGCCTCCCCGGAAAGGAAGTATTTGAGCCTCATTATTACGTATTGCCCGTTAGTCGACAAATCAAGCCCTCGTACGCAGCTTATTCGTACGACGTGGAGGCGTTCCCACGGGCCTAACACGATTGGAACACCACCATAGTAGTGTGGTTCAAATACCTCCTTTGGAGATCTAGAGCTTCACTCTGATTCTAGAGGCAACTTTACAATCGCTCTACGAAATTGTATGGACATCATCAACCGGATATTCTGGGGCGGTAGAATTTCTTTTGTTCGAATCGCTCTAGGCCAGGATCAAATTAATTGAATTGCGGACTCAAGGATCGCGATAGCCGACACATCGGACGCTGTAGAAAGCCAGTCTCTGGATTTAATCCACCCTCTATGTTTGACAAAGCACTAAAACGGGATAGTTTCGGGTGGTATAAGTTTCCCAAGACGATTGCATCGCAATTCATCAACAACCATGAACTTACTGTTTTAGTACTTCCACACACCTTGTTAAATTACGCCTTTACTTCATGTTGCGGTGTGTGTTAGATAGTGTGCAGCTACAAGTCTACCGCCATCGCAGCTCGGGATACCGGCAGATGAGATGGTCCTGAGCTCGTACCGGACTCAAACTTTTTCCTTTACTACCTAGGAATCGCCCATGCGAATTTGTCGGACACACACCATTACATTAACGTCACAACAGCTACTGTTAGAATTTTGCTCTTGCAAATCCTGGAAAGAGTTAAAAAAACTCTTCCGCGCGCCAATAGGGTAAATAATAGATAGCCAGACGGCTGTAAGAGGTGATGACATTTGCAACAATCATGCTGTCGCATCTTCCGCAAGTTCATGTCGCGCCTAGGCAATGGATCTGCGAATGGGGGCCACGGGGTATGAACTACGGAATTCTAAGAAAGTTGCCATCCAGAGTTAAGGGTTTGAGGCTAGTTGCATCGCTGGTAACGAACTACCTCATTACTTGGACGCGCAGTGTGACTTCACTCCTGTATAGCGATGATGCCAAGCAGGAATTAGCAAATCTGAAGAGCGTTTCCAAACTGGCCACTTGGACTGACACCTATCGCGGGGGATTTCAGCGCGTGTCGCTCTCACATGAGAGCTGCCGTCAGGAGCGGTAGAGTTTAGAGAGGAATGCGACAAACTCCCTATTCACCTCTCTGGTGATGTAAGGATATTTACGCTTAGTTCTATGCCAGGCTTAGGGCCTCTCGGAACTTTGGTGAGTCCTTATTAATTGATGCTACCTCTCCCTTACCTTCGCCCCAAGTCACGTAGAAGTACTCAATCCTGCTACATGATAATCAAATATTTCCAACGTTGGGAAATCGGTGACATCACATACTAGTTAAGAAACCACTGTCAGTGAACTTATATCCGGGGGAGAAAATCTACTAACTTACATACGCTGTGCGAGCAGTTTTCATTATAAGAAAATATACTCCCGAGGTACCGCATCAAGCACGACATTCCCGGAGAGCATAACATTTCGGTGCACCTGCTTTTGTGCGCTTGCTTGCGGTTATTTATAAACTACGCACAAGGCGCAAACCGCAGTGCGCATGTTTTCTCCGCCTGGCTAGAACTCGACATTCTCGTCAACGCCAATCTATGTGAGAGGATTTAGACCTCTGTGAAAACGAGTCCCTCTATAGAATAAATACCCAGATGCCAATGGGGGTTCTATCCGATGGCAGTGCATGGAGTGGTGGCTCCAGATTAAGGATGAGGAGAGGTAAAGATAACAGTTCGGTCGCCACGACGCGTTGCCAATCGAAATATCAGTACTAAAAGGCCCACCGCTCCGCTTTAGTCCGACTTTACATCCTGTGGAAATTGTCGAACGGAGGCTACATCGGGCTATATGAGTGTGAAAACCTATACTTCTCGCGTCGTTACTCAGTGCCGGTCTCCTGTTTCCCCCAGTCTTACGTACCCTTATTGATATTTGCTTCACGTTGAAACGTCCTAACGCAGCGTAAAGAGGTGTTTGAACCTCATTACTATAAAATCGCGATCGAAGGTAGACTACATACGCAAACGCCGAAACCCTCAGTTGGCCTTGTTGCAAGTATGGAACGTTGTAAAATTTTTCCTAGACGTTGAGCTATCGGTACAAGGTCGTTAGCGTCCTTACCCTTCACTTATATGCCCGACAAAACGCGGGTCCTAGTGCAGTGGTGGGAGCTTGGAATCCCGCAATACAAGGACAACCTGTATCTCGTTCGGCGTTCCGCGATCACTCGATCCCGAACCACTCCAAGCCTGGTTGATCAGCAAAAGCGGAAGGATGGATAAAGGGCTACTGGTTAATGGATGTAAACTTCCAATGATGAAATCCTGGAAACGAGGGATCGGGTTACGGTGGCGAACGGGGTACGGCAACGTGGCTATCTAGAGCCCGACGTTACGACTCATGTACATGCTGCTACGTGGTTGAAGCTGACGTTCAGATGAAGCAGTACTGAGTCCTAGGGCTTACTACTACTCCAATAGGTCTGGCCGGCCAGATACAAAAGTTCGTGGCGGCTCACCCCCTTTCTGGCGGGTGTAGCTTGCTGACCGGTTTGCTCGATAACACAGGCTAGCGAATAGTAATGAGGTTCGAAAACCTCTTTCCAACGACTGAAAGGGTCTACACGAACTATCTACATTTCCCCGCCCATGTCCTTCCGTCTGGTTGCTTCTGGAGATCCTTTCGCATTATACCGCAGCGTAGTGGCTCTGGCATATATGAAAAAATCCTTCTGTGGGTATTTGTGCCATCACTTATTGTTCGTACCGATATGGGATTACAAGTGCGATGTGATAATAAGCGAAGAAGCCAACATGTTACACTGTTCATGCGCTCCGGGTAATGTGCGGGCACCATGCTCAGTTCCCGCTCGCAGTTGTCACTGTCCCTGTTTCGGCACCATAATCAACATTTCCACGGCCACGCTGGTGAATAACCGAGGATACCGAAGTACAGCAAGAATGAGAGCGGGACTCCTCCATCTGCTTGTAATACGCCTTCAAGATAGTCCATAAAACGGTCGGGGTCTTGTTTCGGACTAGCCGCTTTGAAACGGTGCATAGTTGTGTCAAGTGTGGACATTGGCTTTCTATCCTCGTCAGCGATCCTCGGAAAGACTCGGGCAGTCGCCCCGAATCGTAATTAGGTAGTAGTGCGGCTCAAAAACTTCCTTCGACCTAACCGCTATAATGTTCGTAGATATAAATTTCGTTTCAGTATTAACAGGCGCACCGTATATATACGGAATGGTGTCGCCCCATTAGCTGCTCGCCAATATTTATCTAAGACCGCGCGCGTCTAGCGCCTTTAGTAGTTGCACCCGAGTATAGTAATGGGGTTCGAAGACTTCCTTCGCAAGGCTGCCATACTGTATCACAAGTACTGACGGAGCCCCGGAGGAGTGCAGGATACGGCAAAGGAGACCATTACCGGGGCATGAGTCCAAGTTAGCCCGTTAGGTGAAGGACGCTGATACAATAGTGAATCCGTTACTGAAAGGTTTAGAAGACCGGGGGGCTCGCACTAGGTCCAAATATTATGAACCCTACTCCTGCAACTGAATTGGCCGTCCAGGCGATATTTAAAAGGGGTTACTAGCAGGTTCATCGGAGCCCGTACTCCTTCCGGGCATAGTCGTTCGACGGGTAGAAATTCATCCAGTCGTGCCGGATACCCCGAGAATACCCCTATTTTTTGATCCTTCACCATCATCGTCCGCGGACTCATCTAAGTACCTCAGACCGAAACTGTTATCGTAGCGAAGAGCGAACTCGAATGACATCGCTTGTCCAACAGGGAAAATATGTAAAGTATATGCAGATTATTATAGGAAGATCACAAACTCCATCGCGCCTAGGCCAAAGACTTGCCAGAACAACATCTCTTCCAGAGCAAGGAAGTGTTTGAACCTCACTATTATCGAGAGAAGTCCCATGAATTTATAATAGTGAGGCTCAAAAACTTCCTTCATCGTCGGGCGCTGGGGCGAGCTAGGCTTCCCTAGCCGTCATTACTGTACCCACGCCAAATATTATCGAGTATGACTACGAAGCCTTCACAAGGGGCTGCAGTAACAGACTAACTCACGCACACCGCAACTACTATCCTAAATTGAGTAAGAAAACCCTCGACTATAGCCCTTGAATTAAATTCGCTATTTAAGGAAGACCGCGCTTCCGCTCGCCCGCGTATAGTTTACCAGTCCCAAGAAACATGTGTGGCCAGCCTACCTGAAGAGCTGTGTAAAGATAGATTCTGACATCCTCAAAAAGAAGTTTTCGAGCCGCACTACTACGCACGGAGCTCCGTTATTCAAGGCATGTCGAAGTACAGCGTGGTGGCCTCTCCTGTTCTCCACCCCAGCTAAACCCACCTTGTTCGAATTCGCGCAACTGTATATGACATGAACACTTACAGGGGTTAGAAGTTACTGCAACCAAGATAGAGCTCGTCGAAGTAATAGTGCGGTTCAAAAACTTCCTTCAATTGGTCTCATCACTTAAATTTAAGAGCTATTGTGAGTACAGGTACGGATGCGGCTTCAGTGGATCTTCAGCATTCATTCCTTGTAGTAATGGGGTTCGAAGACTTCCTTGCCAGGGTACCAAACAAGTCTTGCGCATCCTCCTCCCTAAGGAGGTATTTGAACCCCACTATTACCCACGATAGAACATGCAGGGTTTGATAGTGGAACACCTTTTAGAATCTGGGGATAAATTCCCAGGACTAATGTATGGCTGTAGTAATGAGGTTCAAAAACCTCCTTTTCAGGTGGATCGCAGGCCGTGCTGCCTCACAAGCTGGGACGCCGTCCACGGTATAGCCGGCGTCGGCAGTTACTGTGAAATAGCGGAAACTCGATCCCAATATATCATCTTACGTTTGGCGCCCAATAGTCGCCCAGTACCCGTTGACAGTTCTTTAACTCGGCTTAGAACTACTAGACAGGTTCAACCGAACCTTGCCCTAGTTCCCACTCCCGTAATTCATTTGGGTTTGCATCTAGAATACTGGAGGGTGCATAGACGAAACGTGTACGTCGGAGAAAACGTAAGAAAATGACCTAGACTCATAGTAGTGAGGTTCGAAGACTTCCTTTCAGTGAAATCGATCCACCACTCGCCGCGAAGAGATAATAGCATAGAGCACAAGTGCGCGAGTAGAGAAAAAGGCTATCCCAACCGGGCACGTCCTTCGTGTTTGGCGTTTACATACGGCACCCCGTTTCTGCACGTTAACCGTCTAGTATCCAACGGTGGATGGCGGACGCTAGACTATAGATATGAGATATCGAGACCTGGAGCTGGGTGTGGCTGCAGCCCGGGTCATTGCGGGCTGTGAATTCAAGGGCATGTAAACAAGCGTATATCGAACAGTGGATGGGCACCTGCAATACTCACGGTAGAGTTAGCTCACAGGATTCACGTTGAGGACTATGAGTCCCTCTTCGCTAGCAGTCTGGGGGGATATGGAGTTTAATAGCTTGACGTAGTAATGGGGCTCAAACACCTCTTTGTGTGAGCACAGCTACTTGCATTAAGAGATTCTAAACAGCGATCATCTCGGCTATTTCGGGCCAGCCTTTTCGGCAGGATGTTATGTAGCATTTCTGGAAGCTTCCCCCTCGAATCTACTAGTGGTGAGAAGATGCCCCACCGATATTACTCTTTAATCTTGAGAAACCTAAAACCGATCTGACCTCAGACGGGCGGCTCCCACCCGAGGATAAACTCGTCAATAATAATGTGGCTCGAACACTTCTTTTCTCACTAGGCTTTTACGACACGCCACATGTATTTAAGCATCTACCTAACTTGTGTCTGCTGATATACAGCGCATTCTACGCCCAACCTACCAATTACTTCAACGTAGTGCGTGGCTAAAATTCAGGGGAGCTTCATCTCTGTCTTAATTTGAAGGTTCTTCCGGGGCGTTTGGGAATCTTCGTGCCTTTTGCGAGGTTAAGGTATCAAAGAAGTTTTCGAACCACATTATTACCGCCTTAAGCACCGGCGCATCCTGCTCGTGACAACTCTACCCTGCCCTGATAAAGGCACTGAACGTTCCAGAGAGTGCATCATTGACACGCGAGCAGGCCACAGTAGCCACAAGACGTATGGGTGATTATAGAATTGGTGGAGGTGTTGTTAACGATCAGGAGGACATTAGTGGGAGTTAGGAAAGACCCTATGTTCTCTCTATCGCGGACTTGTAACTTGACAAGCAAAAGGGTAAGAGAGCTGCACACCGAAGCAGGCCCTTCCTATACCTGTTTTTCCTACGCGTAGAGAGGAATCCAGAAAGGTGATAATTGGCATTCGATGAAAAAACAGTGTGCCACTGACTTAGTTCTATATGTGAAGAGCCTGTTAGCACGTGACGGCGGCCTTGGTATAGAGCCCTTAATGGTCTCCATCGCGTAGTAATGGGGCTCGAAAACCTCCTTACTTGGGATTGCGTGGCCTCCTTGTGAGTCATACACAAGGCTTAGGGCTATGGGGCGATACACTCCTTTTCGCGGCGCATGGGGCGGTGATGCCTACATAGTAGTAGTGACTGCCTTTCTGGGGGGCTATTTGTGGATGACCAACACCTGACCAGCGATGCAATCGCTAGGGGAGGTACACCTCTCATATGTTACAACAATCACCGAATTGTGTTTCGAATTCGAATCAAGTTTGCGGTGTCGACCAGATCTGGTCTTGCTGCCATACCGGGTTCGCCGCCTCCGGTGGATAGAACTGCATCTTAAGACATCTGGACCCAGCGGTAAGTAGCGGGAAGAGTTTAGAGTCATTCGTACAACTACAGGCTAAGGGCTTACTGGGGAGTTGTTGTAGGGCATAAAGATCGCCCCATGACTTTTCGTACTTTCCCCGATAGTTCACTCGCAGCGAGCTGCGGCTGGGCTTCGCCACACGAGTACGGGCAACATTTATCTCCTCTAATCACTGGGCACCGCGCGAGGAAATAGAAAACCCTAATCAGTGCTCATGGGCGCATCTATTGGTCTCCGCATGCACGATGCCGCGGAGTGCTTAGTTGTCCCTGCATAATCTTCGTAGATGTATAAGAGATTACCTATTTATTCGGTTTCGGTTCTAGACGTACCTTGCCGCATGAGTATAGGCTAATGAACTGAGTTGGCGCCAGAGGGAAAGGCATAATAATGCGGCTCGAATACTTCCTTAAGGAAGTATTCGAACCACATTACTAT".strip())
main(f="Peptide_Encoding_data.txt")
