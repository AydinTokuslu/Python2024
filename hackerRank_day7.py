# Given an array,A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(arr[::-1])
    test_string = ""
    sorted(arr, key=lambda x: (-x[0], x[1]))
    #for i in arr:
    #    res = ''.join(sorted(i, reverse=True))
    #print(str(res))