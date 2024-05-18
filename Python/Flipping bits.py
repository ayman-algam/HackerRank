#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    binary_number = "{0:032b}".format(n)

    inverted_binary_number = ""

    for bit in binary_number:
        if bit == "0":
            inverted_binary_number += "1"
        else:
            inverted_binary_number += "0"

    decimal_number = int(inverted_binary_number, 2)

    return decimal_number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
