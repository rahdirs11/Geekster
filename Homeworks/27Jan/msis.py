# maximum sum increasing subsequence

def maxSumIS(Arr, n):
    msis = [i for i in Arr]
    for i in range(1, n):
        for j in range(i):
            if Arr[i] > Arr[j] and msis[i] < msis[j] + Arr[i]:
                msis[i] = msis[j] + Arr[i]
    
    return max(msis)