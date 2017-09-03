def pickLines(file):
    f = open(file, 'r')
    l = f.readlines()[1::2]
    for i in l:
        print i.strip()
