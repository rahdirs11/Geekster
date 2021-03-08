def appendAndDelete(s, t, k):
    if len(s) + len(t) < k:
        return "Yes"
    
    i = 0
    while i < min(len(s), len(t)) - 1:
        if s[i] != t[i]:
            break
        i += 1
    
    if i == len(s) == len(t):
        return "No" if ((k & 1) == 1) else "Yes"
    
    k = k - (len(s) - 1) - (len(t) - i)

    return "No" if (k < 0 or (k & 1) == 1) else "Yes"
