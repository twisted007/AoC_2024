#!/usr/bin/python

import sys

col1 = []
col2 = []

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for line in lines:
        col1.append(int(line.strip().split()[0]))
        col2.append(int(line.strip().split()[1]))
        
col1_sorted = sorted(col1)
col2_sorted = sorted(col2)
print("Column 1: ",col1_sorted)
print("Column 2: ",col2_sorted)
# print(type(col1_sorted[1]))

count_list = []
# list.count(3)
for num in col1_sorted:
    count_list.append(num * col2_sorted.count(num))

print(count_list)
print("The final sum is: ",sum(count_list))
