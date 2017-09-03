def skew(f):
    f = open(f, "r")

    s = ""
    while True:
        line = f.readline().strip()
        if not line:
            break
        s += line

    Gcount = 0
    Ccount = 0

    
