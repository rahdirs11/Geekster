def permutation(q, a):
    if len(q) == 0:
        print(a)
        return
    
    for i in range(len(q)):
        permutation(q[: i] + q[i + 1: ], a + q[i])
     

permutation("abc", "")