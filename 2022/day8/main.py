import numpy as np

def solve():
    with open('input8.txt', 'r') as f:
        data = f.readlines()
    forest = np.array([[int(x) for x in line.strip()] for line in data])  # get input array

    higher_trees = np.zeros(forest.shape)

    # get the height and width of the forest
    forest_height = forest.shape[0]
    forest_width = forest.shape[1]

    # iterate through the forest, skipping edges
    for i in range(1, forest_height - 1):
        for j in range(1, forest_width - 1):
            # define a tree
            tree = forest[i, j]
            # get all directions (left, right, up, down)
            directions = [forest[i, 0:j], forest[i, j + 1:forest_width], forest[0:i, j], forest[(i + 1):forest_height, j]]
            if any([np.max(direction) < tree for direction in directions]):
                continue
            else:
                higher_trees[i, j] = 1

    return np.size(forest) - np.sum(higher_trees)


print(solve)
