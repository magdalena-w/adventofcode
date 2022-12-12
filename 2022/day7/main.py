from collections import defaultdict

dir_puzzles = []
path = []
sizes = defaultdict(int)
res = 0

with open("input.txt", 'r') as f:
    for line in f:
        dir_puzzles.append(line.strip())

for line in dir_puzzles:
    if line.startswith('$ cd'):
        # Get only dir name
        directory = line.split()[-1]
        if directory == '..':
            path.pop()
        else:
            path.append(directory)
    elif line.startswith('$ ls'):
        continue
    else:
        size, _ = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += size

# Part 1
for i in sizes:
    if sizes[i] <= 100000:
        res += sizes[i]
print(f"Part 1 result: {res}")

# Part 2

# Find the size of the outermost directory
values = list(sizes.values())
outermost_dir = values[0]
# To run the update, you need unused space of at least 30000000
needed_space = 30000000 - (70000000 - outermost_dir)

smallest = []

for i in sizes:
    if sizes[i] >= needed_space:
        smallest.append(sizes[i])

print(f"Part 2 result: {min(smallest)}")