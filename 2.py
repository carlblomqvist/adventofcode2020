#!/usr/bin/env python3

#

# Input format:
# 1-2 x: string
# lowest-highest number of occurences of x in string

# Get lines
with open("2.input") as f:
    lines = [i.strip() for i in f.readlines()]

# Parse lines
i = 0
passwords = []
for line in lines:
    array = line.split('-')
    array = [array[0]] + array[1].split()
    passwords.append([array[0], array[1], array[2].strip(':'), array[3]])


# Part 1: Calculate number of correct passwords
count = 0
for obj in passwords:
    min = int(obj[0])
    max = int(obj[1])
    letter = obj[2]
    password = obj[3]
    occurences = password.count(letter)
    if (occurences >= min and occurences <= max):
        count = count + 1

print(count)

# Part 2: Calculate number of correct passwords with the NEW policy
count = 0
for obj in passwords:
    first = int(obj[0])
    second = int(obj[1])
    letter = obj[2]
    password = obj[3]
    has_first = password.count(letter, first-1, first)
    has_second = password.count(letter, second-1, second)
    if ((has_first + has_second) == 1):
        count = count + 1

print(count)
