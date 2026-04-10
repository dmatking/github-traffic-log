#!/usr/bin/env python3
# Upsert new daily traffic rows into traffic.csv.
# Usage: python3 upsert_traffic.py <new_rows_file>
# Replaces any existing (date, repo) rows with fresh data, keeps the rest.

import csv, sys

new_rows = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        new_rows[(parts[0], parts[1])] = parts

existing = {}
try:
    with open('traffic.csv', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            existing[(row[0], row[1])] = row
except FileNotFoundError:
    header = ['date','repo','views','view_uniques','clones','clone_uniques','stars','forks']

existing.update(new_rows)

with open('traffic.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for key in sorted(existing.keys()):
        writer.writerow(existing[key])
