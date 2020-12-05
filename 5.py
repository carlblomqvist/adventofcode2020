#!/usr/bin/env python3
import re

# Input format:

# The first 7 characters will either be F or B; these specify exactly one of the
# 128 rows on the plane (numbered 0 through 127). Each letter tells you which half
# of a region the given seat is in. Start with the whole list of rows; the first
# letter indicates whether the seat is in the front (0 through 63) or the back (64
# through 127). The next letter indicates which half of that region the seat is
# in, and so on until you're left with exactly one row.

# The last three characters will be either L or R; these specify exactly one of
# the 8 columns of seats on the plane (numbered 0 through 7). The same process as
# above proceeds again, this time with only three steps. L means to keep the lower
# half, while R means to keep the upper half.

# Get data
with open("5.input") as f:
    lines = [i.strip() for i in f.readlines()]

# Helper functions
def binpart(l, r, direction):
    t = 0
    if (direction == "F" or direction == "L"):
        t = (l + r) // 2
        return l, t
    elif (direction == "B" or direction == "R"):
        t = ((l + r) // 2) + 1
        return t, r

# Validate data
# Part 1
boarding = []
for line in lines:
    f = 0
    b = 127
    l = 0
    r = 7
    for c in line:
        if (not f == b):
            f, b = binpart(f, b, c)
        else:
            l, r = binpart(l, r, c)
    boarding.append([f, l, ((f * 8) + l)])
    assert(f == b)
    assert(l == r)

highest = 0
for b in boarding:
    if (b[2] > highest):
        highest = b[2]

print(f"The highest seat ID is: {highest}")

# Part 2: SO NAIVE
candidates = []
for a in boarding:
    for b in boarding:
        if a[2] == (b[2] + 2):
            if (a[1] + 1 == 8): # We only have 7 columns
                break
            candidates.append([a[0], a[1] + 1, (a[0] * 8 + (a[1] + 1) )])

for c in candidates:
    found = False
    for a in boarding:
        if a == c:
            found = True

    if not found:
        print(f"Our seat ID is {c[2]}")
