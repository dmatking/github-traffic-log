#!/usr/bin/env python3
# Generate totals.csv with cumulative all-time sums per repo from traffic.csv.
# Stars and forks take the most recent date's value (traffic.csv is date-sorted).

import csv
from collections import defaultdict

totals = defaultdict(lambda: [0, 0, 0, 0])
stars  = {}
forks  = {}

with open('traffic.csv', newline='') as f:
    for row in csv.DictReader(f):
        r = row['repo']
        totals[r][0] += int(row['views'])
        totals[r][1] += int(row['view_uniques'])
        totals[r][2] += int(row['clones'])
        totals[r][3] += int(row['clone_uniques'])
        stars[r] = row['stars']
        forks[r] = row['forks']

with open('totals.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['repo','views','view_uniques','clones','clone_uniques','stars','forks'])
    for r in sorted(totals):
        t = totals[r]
        w.writerow([r, t[0], t[1], t[2], t[3], stars[r], forks[r]])
