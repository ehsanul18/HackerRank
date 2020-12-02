#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    c=0
    roundup_grades=[]
    for i in range(len(grades)):
        if(grades[i]<38):
            roundup_grades.append(grades[i])
        else:
            c=grades[i]
            if(c%5!=0):
                print(c)
                while(c%5!=0):
                    c+=1 
                if((c-grades[i])<3):
                    roundup_grades.append(c)
                else:
                    roundup_grades.append(grades[i])
            else:
                roundup_grades.append(grades[i])
    return roundup_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
