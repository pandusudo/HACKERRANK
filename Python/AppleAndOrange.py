# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
# In the diagram below, the red region denotes his house, where S is the start point, and T is the endpoint. 
# The apple tree is to the left of his house, and the orange tree is to its right. 
# You can assume the trees are located on a single point, where the apple tree is at point A, and the orange tree is at point B.
# 
# When a fruit falls from its tree, it lands D units of distance from its tree of origin along the X-axis. 
# A negative value of D means the fruit fell D units to the tree's left, and a positive value of D means it falls D units to the tree's right. 
# Given the value of D for M apples and N oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    orangeCount = 0
    appleCount = 0

    for i in range(len(oranges)):
        if(oranges[i] + b >= s and oranges[i] + b <= t):
            orangeCount += 1

    for j in range(len(apples)):
        if(apples[j] + a >= s and apples[j] + a <= t):
            appleCount += 1
            
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
