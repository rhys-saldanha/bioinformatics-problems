#count number of subtrings in strings

def subs(file):
    f = open(file, 'r')
    s = f.readline().strip()
    t = f.readline().strip()
    
    s_num = len(s)
    t_num = len(t)
    l = ''

    for i in range(s_num):
        if s[i:i+t_num] == t:
            l += str(i+1) + ' '

    print l

subs('rosalind_subs.txt')
