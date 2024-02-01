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
a = open("test.txt", "w")
def replace_lingual_numbers(data):
    ptr = 0
    print(data)
    a.write(data +"\n")
    while ptr != len(data):
        ptr_step = 1

        for number_word in english_numbers.keys():
            ptr_end = ptr + len(number_word)
            
            if ptr_end > len(data):
                continue

            if data[ptr:ptr_end] == number_word:
                number = english_numbers[number_word]
                data = data[:ptr] + number + data[ptr_end:]
                ptr_step = len(number)
                break

        ptr += ptr_step
    print(data)
    a.write(data +"\n")
    return data


total = 0

with open("1.input.txt") as input_file:
    for line in input_file:
        line = line.strip()

        # part 2: some numbers are of their words
        line = replace_lingual_numbers(line)

        line_numbers = strip_alphabetical(line)
        
        a.write(line_numbers +"\n")
        line_first_and_last_numbers = first_and_last_chars(line_numbers)
        
        a.write(line_first_and_last_numbers +"\n")
        total += int(line_first_and_last_numbers)

a.close()


print("Total: %d" % total)