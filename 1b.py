import re

def strip_alphabetical(data):
    return re.sub(r'[A-Za-z]', '', data)

def first_and_last_chars(data):
    return data[0] + data[-1]

# part 2: some numbers are of their words
english_numbers = {
    "oneight": "18",
    "twone": "21",
    "eightwo": "82",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def replace_lingual_numbers(data):
    for number_word, number in english_numbers.items():
        data = data.replace(number_word, number)
    return data

total = 0

with open("1.input.txt") as input_file:
    for line in input_file:
        line = line.strip()

        # part 2: some numbers are of their words
        line = replace_lingual_numbers(line)

        line_numbers = strip_alphabetical(line)
        
        line_first_and_last_numbers = first_and_last_chars(line_numbers)
        
        total += int(line_first_and_last_numbers)

print("Total: %d" % total)