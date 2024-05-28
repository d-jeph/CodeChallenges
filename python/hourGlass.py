# Hackerrank Link = https://www.hackerrank.com/challenges/2d-array/problem

import math 

def hourglassSum(arr):
    # Write your code here
    max_sum = -math.inf
    m = 4
    for row in range(m):
            for col in range(m):
                hour_glass_sum = \
                arr[row][col] + arr[row][col+1] + arr[row][col+2] + \
                arr[row+1][col+1] + \
                arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
                max_sum = max((max_sum, hour_glass_sum))
    return max_sum
    