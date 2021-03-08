#!/usr/bin/env python3

def staircase(n: int):
    row, cst, nst = 1, 1, 1
    while row <= n:
        spaces = n - row
        while spaces >= 1:
            print(' ', end="")
            spaces -= 1
        cst = 1
        while cst <= nst:
            print('#', end="")
            cst += 1
        print()
        row += 1
        nst += 1

staircase(int(input()))
