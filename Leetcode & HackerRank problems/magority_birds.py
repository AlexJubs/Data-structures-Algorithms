#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr, first=True):
    table = {}
    res = arr[0]
    for x in arr:
        if x not in table: table[x] = 0
        table[x] = table[x]+1
        if table[x] > table[res]:
            if first: res = x
            else: res = min(res,x)

    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
