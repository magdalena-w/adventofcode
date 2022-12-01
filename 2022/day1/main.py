elves_calories = []
sum_calories = 0

with open('day1/calories.txt', 'r') as c:
    for line in c:
        line = line.strip()
        if line != '':
            sum_calories += int(line)
        else:
            elves_calories.append(sum_calories)
            sum_calories = 0
elves_calories.sort()

print(f"Elf carrying the most Calories: {elves_calories[-1]}")
print(f"Total calories carrying by top three elves: {sum(elves_calories[-3:])}")
