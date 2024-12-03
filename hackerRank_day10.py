# Given a base-10 integer, n, convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number
# of consecutive 1's in n's binary representation.
# When working with different bases, it is common to show the base as a subscript.

# input :5
# output : 1
# input:13
# output:2

import math
import os
import random
import re
import sys


def max_consecutive_ones(n):
    binary_representation = bin(n)[2:]
    ones_sequences = binary_representation.split('0')
    max_ones = max(len(seq) for seq in ones_sequences)
    return max_ones


if __name__ == '__main__':
    n = int(input().strip())
    result = max_consecutive_ones(n)
    print(result)