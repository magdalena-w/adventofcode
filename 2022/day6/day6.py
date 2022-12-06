with open("input.txt", 'r') as f:
    buffer = f.read()


def get_marker(length):
    for i, char in enumerate(buffer):
        unique_str = buffer[i:i+length]
        if len(set(unique_str)) == length:
            return i + length


print(f"Part1: {get_marker(4)}")
print(f"Part1: {get_marker(14)}")