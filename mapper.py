#!/usr/bin/env python
import sys

for line in sys.stdin:
    if "Nationality" in line:
        continue
    data = line.strip().split(',')
    try:
        nationality = data[4]   # Nationality column (index 4 in FIFA22_official_data.csv)
        overall = float(data[6])  # Overall column (index 6 in FIFA22_official_data.csv)
        print("%s\t%s" % (nationality, overall))
    except (IndexError, ValueError):
        continue
