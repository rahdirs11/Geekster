N, M = map(int, input().split())
superset, subset = dict(), dict()

X = input().split()
Y = input().split()
for x in X:
    superset[x] = superset.get(x, 0) + 1

for y in Y:
    subset[y] = subset.get(y, 0) + 1


for y in Y:
    if not superset.get(y, 0) == subset.get(y):
        print('NO')
        break
else:
    print('YES')
