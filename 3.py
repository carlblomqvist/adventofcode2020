#!/usr/bin/env python3

#

# Input format:
# map where . is open, and # is a tree.
# How many trees do we encounter when moving right 3, down 1 until we're past the last row?

# Get lines
with open("3.input") as f:
    lines = [i.strip() for i in f.readlines()]

# Counts of rows/columns
rows = len(lines) - 1 # Because of zero indexing
columns = len(lines[0]) # Because of modulo

# Part 1: Calculate number of trees we hit.
r = 0
c = 0
hits = 0
while (r < rows):
    r = r + 1
    c = (c + 3) % columns
    hits = hits + lines[r].count('#', c, c + 1)

print(hits)

# Part 2: Calculate more paths
first_path = 0
r = 0
c = 0
while (r < rows):
    r = r + 1
    c = (c + 1) % columns
    first_path = first_path + lines[r].count('#', c, c + 1)

second_path = 0
r = 0
c = 0
while (r < rows):
    r = r + 1
    c = (c + 5) % columns
    second_path = second_path + lines[r].count('#', c, c + 1)

third_path = 0
r = 0
c = 0
while (r < rows):
    r = r + 1
    c = (c + 7) % columns
    third_path = third_path + lines[r].count('#', c, c + 1)

fourth_path = 0
r = 0
c = 0
while (r < rows):
    r = r + 2
    c = (c + 1) % columns
    fourth_path = fourth_path + lines[r].count('#', c, c + 1)

print(f"All paths multiplied: {first_path * second_path * third_path * fourth_path * hits}")
