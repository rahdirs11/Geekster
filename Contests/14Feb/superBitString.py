def superStrings(string):
    if len(string) == 0:
        return ['']
    
    ch = string[0]
    remaining = superStrings(string[1:])

    current = []

    for x in remaining:
        current.append('1' + x)
        if ch == '0':
            current.append('0' + x)
    
    return current


# print(superStrings('010'))

n, k = int(input()), int(input())

binary = ''
while k != 0:
    binary = str(k % 2) + binary
    k //= 2

# print(binary)

if len(binary) < n:
    a = 1
    while a <= n - len(binary):
        binary = '0' + binary
# appending extra zeros

output = superStrings(binary)

for i in range(len(output) - 1, -1, -1):
    print(output[i])
