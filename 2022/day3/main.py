import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

with open("file.txt", 'r') as f:
    results = 0
    for line in f:
        rucksack = line.strip()
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]

        for letter in values:
            if letter in first_half and letter in second_half:
                results += values[letter]

print(f"Result part1: {results}")
