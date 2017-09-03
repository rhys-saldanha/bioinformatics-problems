def oddAdd(a,b):
    f = 0
    for i in range(a,b+1):
        if i%2 == 1:
            f+=i
    return f
