#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    maxValue = s - arr[0]
    minValue = s - arr[len(arr) - 1]
    
    print(minValue, maxValue)

        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
