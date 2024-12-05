# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
#
# Example
#
# In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.
#
# Input Format
#
# There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    def max_hourglass_sum(arr):
        max_sum = float('-inf')  # Initialize to a very small number

        # Loop over the array to find all hourglasses
        for i in range(4):  # Rows (0 to 3)
            for j in range(4):  # Columns (0 to 3)
                # Calculate the sum of the hourglass
                print(f"i = {i}")
                print(f"j = {j}")
                top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                middle = arr[i + 1][j + 1]
                bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

                hourglass_sum = top + middle + bottom

                # Update max_sum if a larger sum is found
                max_sum = max(max_sum, hourglass_sum)

        return max_sum


    # Output the result
    print(max_hourglass_sum(arr))