def iprb(k,m,n):
    k = float(k)
    m = float(m)
    n = float(n)
    pop = k + m + n
    pop_base = pop * 4
    k_base = 4
    m_base = 4
    n_base = 1
    print ((k*k_base) + (m*m_base) + (n*n_base))/pop_base
    
