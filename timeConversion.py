#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    conv = s.split(":")
    if s[-2:] == "PM":
        if conv[0] != "12":
            conv[0] = str(int(conv[0])+12)
    else:
        if conv[0] == "12":
            conv[0] = "00"
    hour24 = ':'.join(conv)
    return str(hour24[:-2])
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
