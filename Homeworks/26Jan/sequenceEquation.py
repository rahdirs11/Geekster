def permutationEquation(p: list):
    result = []
    for i in range(1, len(p) + 1):
        iIndex = p.index(i)
        result.append(p.index(iIndex + 1) + 1)
    
    return result

n = int(input())
p = [int(x) for x in input().split()]

print(permutationEquation(p))