#!/usr/bin/env python3


import sys
import os
import csv


# Show input
with open(sys.argv[1], 'r', newline='') as testfile:
    print(testfile.read())

print("============================")

# Read for converting
f = open(sys.argv[1], 'r')
lines = f.readlines()

new_line = []
rows = []

for line in lines:
    if len(line) == 1 and ord(line[0]) == 10:
        # Next file indication
        if len(new_line):
            rows.append(new_line)

        new_line = []
        continue

    new_line.append(line.strip())


# Write converted
with open(sys.argv[1] + ".csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')

    for r in rows:
        spamwriter.writerow(r)

# Show converted
print("Output in", sys.argv[1] + ".csv")
print("============================")
with open(sys.argv[1] + ".csv", 'r', newline='') as testfile:
    print(testfile.read())

