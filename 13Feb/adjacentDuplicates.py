def removeDuplicates(arr: list):
    '''
    Removing adjacent duplicates from an array
    '''
    stack = []
    for a in arr:
        if len(stack) !=0 and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    
    # stack.reverse()

    print(stack if len(stack) != 0 else -1)

# removeDuplicates([1, 2, 2, 2, 1])
# removeDuplicates([1, 2, 2, 1, 3, 4, 4, 3])
# removeDuplicates([1, 1, 3, 3])
removeDuplicates([1, 2, 2, 1, 3, 4, 4, 4])