import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

with open("file.txt", 'r') as f:
    results = 0
    rucksack = f.readlines()
    for i in range(0, len(rucksack), 3):
        a, b, c = rucksack[i], rucksack[i+1], rucksack[i+2]
        for letter in values:
            if (letter in a) and (letter in b) and (letter in c):
                results += values[letter]

print(f"Result part2: {results}")


