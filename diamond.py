def diamond(line: int):
    row, nst = 1, 1
    while row <= 2 * line - 1:
        # spaces = max(line, row) - min(line, row)
        # while spaces >= 1:
        #     print(' ', end='')
        #     spaces -= 1
        cst = 1
        print(f'row = {row}', f'nst = {nst}, {nst // 2 + 1}', sep="\n")
        nst = nst + 2 if row < line else nst - 2
        row += 1


diamond(4)
