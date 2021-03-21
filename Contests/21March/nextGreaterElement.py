n, m = map(int, input().split())
nums1, nums2 = list(map(int, input().split())), list(map(int, input().split()))

stack = []

nge = {
    i: -1
    for i in nums1
}
print(nge)

for i in nums2:
    while len(stack) and stack[-1] < i:
        x = stack.pop()
        # print(x)
        if x in nge:
            nge[x] = i

    stack.append(i)
    # print(f'Stack -> {stack}')

for n in nums1:
    print(nge[n], end=" ")
