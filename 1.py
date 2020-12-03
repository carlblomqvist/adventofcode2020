#!/usr/bin/env python3

# Pretty spammy output, but it works

with open("1.input") as f:
    lines = [int(i.strip()) for i in f.readlines()]

# Part 1
for line in lines:
    current = line
    want = 2020 - line
    for other in lines:
        if (other == want):
            print(f'Day 1.1: {current * other}')
            break

# Part 2
for line in lines:
    first = line
    want_sum = 2020 - line
    for second in lines:
        want = want_sum - second
        for third in lines:
            if (third == want):
                print(f'Day 1.2: {first * second * third}')
                break
