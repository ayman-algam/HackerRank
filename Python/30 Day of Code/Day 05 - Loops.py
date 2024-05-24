#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    [print("{} x {} = {}".format(n, x, n * x)) for x in range(1, 11)]
