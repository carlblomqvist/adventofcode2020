#!/usr/bin/env python3
import re

# Input format:
# The automatic passport scanners are slow because they're having trouble
# detecting which passports have all required fields. The expected fields are as
# follows:

#     byr (Birth Year)
#     iyr (Issue Year)
#     eyr (Expiration Year)
#     hgt (Height)
#     hcl (Hair Color)
#     ecl (Eye Color)
#     pid (Passport ID)
#     cid (Country ID) - OPTIONAL

# Passport data is validated in batch files (your puzzle input). Each passport is
# represented as a sequence of key:value pairs separated by spaces or newlines.
# Passports are separated by blank lines.

# Get data
with open("4.input") as f:
    data = f.read().split("\n\n")

# Parse data
passports = []
for entry in data:
    passports.append(entry.split())

entries = []
i = 0
for entry in passports:
    entries.append({})
    for field in entry:
        key, val = field.partition(":")[::2]
        entries[i][key.strip()] = val

    i = i+1

# Validate data
def valid(p):
    try:
        result = p["byr"] and p["iyr"] and p["eyr"] and p["hgt"] and p["hcl"] and p["ecl"] and p["pid"]
        return result
    except KeyError:
        return 0

valid_passports = 0
for entry in entries:
    if (valid(entry)):
        valid_passports = valid_passports + 1

print(f"Number of valid passwords for part 1: {valid_passports}")


    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

# Validate data for part 2
def valid2(p):
    try:
        byr = int(p["byr"])
        byr = (byr >= 1920 and byr <= 2002)

        iyr = int(p["iyr"])
        iyr = (iyr >= 2010 and iyr <= 2020)

        eyr = int(p["eyr"])
        eyr = (eyr >= 2020 and eyr <= 2030)

        temp = re.compile("([0-9]+)([a-z]+)")
        temp = temp.match(p["hgt"])
        unit = 0
        hgt = 0
        if (temp):
            hgt, unit = temp.groups()
        if (unit):
            hgt = int(hgt)
            if (unit == "cm"):
                hgt = (hgt >= 150 and hgt <= 193)
            elif (unit == "in"):
                hgt = (hgt >= 59 and hgt <= 76)
            else:
                hgt = 0

        hcl = p["hcl"]
        hcl = re.search("^#([a-f]|[0-9]){6}$", hcl)

        ecl = p["ecl"]
        ecl = re.search("amb|blu|brn|gry|grn|hzl|oth", ecl)

        pid = p["pid"]
        pid = re.search("^[0-9]{9}$", pid)

        return byr and iyr and eyr and hgt and hcl and ecl and pid

    except KeyError:
        return 0

valid_passports2 = 0
for entry in entries:
    if (valid2(entry)):
        valid_passports2 = valid_passports2 + 1

print(valid_passports2)
