str1, str2 = input(), input()

freq = {}
for l in str1:
    freq[l] = freq.get(l, 0) + 1

maxChar = list(freq.keys())[list(freq.values()).index(max(freq.values()))]
# print(maxChar)

print('Yes' if str2.count(maxChar) == freq[maxChar] else 'No')
