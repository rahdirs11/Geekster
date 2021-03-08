def trap(arr):
    lmax = [0 for i in range(len(arr))]
    rmax = [0 for i in range(len(arr))]
    lmax[0] = arr[0]
    rmax[len(arr) - 1] = arr[len(arr) - 1]
    for i in range(1, len(arr)):
        lmax[i] = max(lmax[i - 1], arr[i])
    
    for i in range(len(arr) - 2, -1, -1):
        rmax[i] = max(rmax[i + 1], arr[i])
    
    ans = 0
    for i in range(len(arr)):
        minVal = min(lmax[i], rmax[i])

        if minVal > arr[i]:
            ans += minVal - arr[i]
    
    return ans

print(trap([1,8,6,2,5,4,8,3,7]))