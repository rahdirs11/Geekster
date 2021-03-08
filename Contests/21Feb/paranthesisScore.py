'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
'''



def calculateScore(string, start, end):
    ans, balanced = 0, 0
    for i in range(start, end):
        balanced = balanced + 1 if string[i] == '(' else balanced - 1
        if balanced == 0:
            if i - start == 1:
                ans += 1
            else:
                ans += 2 * calculateScore(string, start + 1, i)
            start = i + 1
    return ans


string = input()
print(calculateScore(string, 0, len(string)))