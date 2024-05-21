#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    the_result = ""
    for i in range(n - 1, -1, -1):
        the_result = the_result + str(arr[i]) + " "

    print(the_result)
