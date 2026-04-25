#!/usr/bin/env python
import sys

current_nationality = None
total = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    if '\t' not in line:
        continue
    nationality, overall = line.split('\t')
    overall = float(overall)

    if current_nationality == nationality:
        total += overall
        count += 1
    else:
        if current_nationality:
            print("%s\t%.2f" % (current_nationality, total / count))
        current_nationality = nationality
        total = overall
        count = 1

if current_nationality:
    print("%s\t%.2f" % (current_nationality, total / count))
