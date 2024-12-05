#!/usr/bin/python

import sys

col1 = []
col2 = []



with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    # print(map(line.split() for line in lines))
    v = []
    for line in lines:
        # print(type(line))
        # print(line.strip().split())
        col1.append(int(line.strip().split()[0]))
        col2.append(int(line.strip().split()[1]))
        
# print(type(lines))
col1_sorted = sorted(col1)
col2_sorted = sorted(col2)
print("Column 1: ",col1_sorted)
print("Column 2: ",col2_sorted)
# print(type(col1_sorted[1]))
absval = [abs(a-b) for a,b in zip(col1_sorted, col2_sorted)]
final = 0
for num in absval:
    final += num

print("The final result is: ",final)