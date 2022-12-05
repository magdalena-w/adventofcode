stack1 = ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q']
stack2 = ['W', 'D', 'B', 'G']
stack3 = ['F', 'W', 'R', 'T', 'S', 'Q', 'B']
stack4 = ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N']
stack5 = ['M', 'P', 'D', 'V', 'F']
stack6 = ['F', 'W', 'J']
stack7 = ['L', 'N', 'Q', 'B', 'J', 'V']
stack8 = ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N']
stack9 = ['J', 'S', 'Q', 'C', 'W', 'D', 'M']

stack_map = {
    1: stack1, 2: stack2, 3: stack3,
    4: stack4, 5: stack5, 6: stack6,
    7: stack7, 8: stack8, 9: stack9,
}


with open("moves.txt", 'r') as f:
    for line in f:
        # Getting the format: [1, 2, 3]
        lines = line.strip().replace("move", "").replace("from", ",").replace("to", ",").replace(" ", "").split(",")
        lines = [int(i) for i in lines]

        # move lines[0] from lines[1] to lines[2]

        items_num = lines[0]
        from_stack_num = lines[1]
        to_stack_num = lines[2]

        while items_num > 0:
            current = stack_map[from_stack_num][-1]
            stack_map[from_stack_num].pop()
            stack_map[to_stack_num].append(current)
            items_num -= 1

# Print crates on top of each stack
for x in stack_map:
    print(stack_map[x][-1])