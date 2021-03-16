'''
At every level k, there are exactly k stones.
Find the number of stairs you can form with given number of
stones
'''

def stairs(n: int):
    count, level = 1, 1
    stairs = 0
    while count <= n:
        stairs += 1
        level += 1
        count += level

    return stairs

for _ in range(int(input())):
    print(stairs(int(input())))
