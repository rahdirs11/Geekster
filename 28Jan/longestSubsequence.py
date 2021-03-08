def sequence(arr, target, index, res):
    if len(arr) == index:
        if target == 0:
            print(res)
        else:
            return

    sequence(arr, target, index + 1, res)
    sequence(arr, target - arr[index], index + 1, res.append(arr[index]))


sequence([10, 20, 30, 40, 5, 11, 6, 9], 60, 0, [])