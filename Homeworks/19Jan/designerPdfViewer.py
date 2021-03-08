#!/usr/bin/env python3

def highlightedArea(h: list, word: str) -> int:
    maxHeight = 0
    for letter in word:
        lh = h[ord(letter) - 97]
        maxHeight = lh if lh > maxHeight else maxHeight
    return maxHeight * len(word)


h = list(map(int, input().split()))
word = input()

print(highlightedArea(h, word))
