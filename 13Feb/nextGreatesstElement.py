def nextGreatest(arr):
    stack = []
    for num in arr:
        while len(stack) != 0 and stack[-1] < num:
            print(stack.pop(), ' -> ', num, end=" | \n")
        stack.append(num)
    while len(stack) != 0:
        print(stack.pop(), ' -> ', -1, end=" | \n")

nextGreatest([1, 2, 13, 4, 6, 16, 0])