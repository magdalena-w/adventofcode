fully_contains = 0
partially_contains = 0

with open("file.txt", 'r') as file:
    for line in file:
        pair = line.strip().replace("-", ",").split(",")
        pair = [int(i) for i in pair]

        if (pair[2] >= pair[0]) and (pair[3] <= pair[1]):
            fully_contains += 1
        elif (pair[0] >= pair[2]) and (pair[1] <= pair[3]):
            fully_contains += 1

        if (pair[1] < pair[2]) or (pair[0] > pair[3]):
            pass
        else:
            partially_contains += 1

print(f"Full overlaps: {fully_contains}")
print(f"Part overlap: {partially_contains}")
