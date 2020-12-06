#!/usr/bin/env python3
import re

# Input format:

# Each group's answers are separated by a blank line, and within each group, each
# person's answers are on a single line.

# Get data
with open("6.input") as f:
    data = f.read().split("\n\n")

# edit for part 2: separate users
new_data = []
for entry in data:
    new_data.append(entry.split('\n'))

# we don't care about separating the users, right? (edit: only for part 1 it seems...)
# I'll leave this here anyway
data = [i.replace('\n', '') for i in data]

# Parse data - for Part 1
customs = []
for i, entry in enumerate(data, start=0):
    customs.append(set())
    for c in entry:
        customs[i].add(c)

total = 0
for entry in customs:
    total = total + len(entry)

print(f"Total number of 'yes': {total}")

# Parse data - for Part 2
customs = []
for i, entry in enumerate(new_data, start=0):
    customs.append([])
    for person in entry:
        customs[i].append(set(person))

# Intersect sets
for entry in customs:
    for i in range(len(entry)):
        entry[0].intersection_update(entry[i])

total = 0
for entry in customs:
    total = total + len(entry[0])

print(f"Total number of 'yes' per group: {total}")
