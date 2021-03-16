#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        # fptr.write(str(node.data))
        print(node.data, end="")

        node = node.next

        if node:
            # fptr.write(sep)
            print(end=" ")

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST List
#  2. INTEGER N
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def solve(List, N):
    if List == None:
        return None

    curr, n, p = List, None, None
    nodeCount = 0
    while nodeCount < N and curr is not None:
        n = curr.next
        curr.next = p
        p = curr
        curr = n
        nodeCount += 1

    if n is not None:
        List.next = solve(n, N)

    return p
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l_count = int(input().strip())

    l = SinglyLinkedList()

    for _ in range(l_count):
        l_item = int(input().strip())
        l.insert_node(l_item)

    n = int(input().strip())

    result = solve(l.head, n)

    print_singly_linked_list(result, ' ')
    # fptr.write('\n')

    # fptr.close()
