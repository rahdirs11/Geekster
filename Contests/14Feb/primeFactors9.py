n = int(input())
t = n
factors = []

p = 2
xor = -1

while p <= n // 2:
    if n % p == 0:
        factors.append(p)
        while t % p == 0:
            t //= p
    
    p += 1

if len(factors) == 0:
    print(n ^ 0)
else:
    xor = factors[0]
    # print(factors)
    for i in range(1, len(factors)):
        xor ^= factors[i]
    print(xor)