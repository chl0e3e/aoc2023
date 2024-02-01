import re

def strip_alphabetical(data):
    return re.sub(r'[A-Za-z]', '', data)

def first_and_last_chars(data):
    return data[0] + data[-1]

total = 0

with open("1.input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        line_numbers = strip_alphabetical(line)
        line_first_and_last_numbers = first_and_last_chars(line_numbers)
        total += int(line_first_and_last_numbers)

print("Total: %d" % total)