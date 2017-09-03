def wordCount(file):
    d = {}
    f = open(file, 'r')
    s = f.read()
    for word in s.split():
        if word in d:
            d[word]+=1
        if word not in d:
            d[word] = 1
    for key, value in d.items():
        print key + ' %s' % value
