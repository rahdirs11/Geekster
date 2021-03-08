def encryption(s: str):
    ListOfWords = s.strip().split()
    newStr = ''.join(ListOfWords)
    # print(len(words))
    from math import ceil, sqrt, floor
    root = sqrt(len(newStr))
    rows, cols = floor(root), ceil(root)
    if rows * cols < len(newStr):
        rows = cols
    # print(f'Rows:\t{rows} || Columns:\t{cols}\nOld String:\t{s} || New String:\t{newStr}\n', end="====================\n")
    reformed = []
    index = 0
    while index < len(newStr):
        row = ""
        while len(row) < cols:
            # print(newStr[index], end="")
            row += newStr[index]
            index += 1
            if index == len(newStr) and len(row) < cols:
                for i in range(cols - len(row)):
                    row += " "
                    # print(' ', end="")
                break
        # print()
        reformed.append(row)

    # print(reformed)
    encryptedStr = ""
    for i in range(cols):
        for j in range(rows):
            encryptedStr += reformed[j][i]
        
        encryptedStr = encryptedStr.rstrip() +  " "
    
    return encryptedStr.rstrip()


message = input()

print(encryption(message))


