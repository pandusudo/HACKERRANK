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
