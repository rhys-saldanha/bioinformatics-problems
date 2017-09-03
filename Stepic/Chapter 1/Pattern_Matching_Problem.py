#count number of subtrings in strings
import sys

def subs(f):
    f = open(f, 'r')
    t = f.readline().strip()
    print t
    s = ''
    while True:
        line = f.readline().strip()
        if not line:
            break
        else:
            s += line
    s_num = len(s)
    t_num = len(t)
    l = ''

    for i in range(s_num):
        if s[i:i+t_num] == t:
            l += str(i) + ' '
    print l

def subsKmer(f, k):
    f = open(f, 'r')
    t = k
    print t
    s = ''
    while True:
        line = f.readline().strip()
        if not line:
            break
        else:
            s += line
    s_num = len(s)
    t_num = len(t)
    l = ''

    for i in range(s_num):
        if s[i:i+t_num] == t:
            l += str(i) + ' '
    print l

try:
    subsKmer(sys.argv[2], sys.argvs[3])
except IndexError:
    try: subs(sys.argv[2])
    except IndexError:
        if raw_input('Would you like to input kmer? (y/n): ').lower() == 'y':
            subsKmer(raw_input('File name: '), raw_input('kmer: '))
        else:
            subs(raw_input('File name: '))
