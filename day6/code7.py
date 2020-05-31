def A(p, q, r ="% s"): 
    print(r % ("A(% d, % d)" % (p, q))) 
    if p == 0: 
        return q + 1
    if q == 0: 
        return A(p - 1, 1, r) 
    ab = A(p, q - 1, r % ("A(% d, %% s)" % (p - 1))) 
    return A(p - 1, ab, r) 
  
print(A(1, 2))
