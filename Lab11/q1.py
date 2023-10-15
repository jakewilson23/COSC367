"""Write two functions max_value(tree) and min_value(tree) that given a game tree, return the utility of the root of
the tree when the root is a max node or min node correspondingly. Process the children of a node from left (lower
index) to right (higher index)."""


def max_value(tree):
    if isinstance(tree, int):
        return tree
    value = float("-inf")
    for child in tree:
        value = max(value, min_value(child))
    return value


def min_value(tree):
    if isinstance(tree, int):
        return tree
    value = float("inf")
    for child in tree:
        value = min(value, max_value(child))
    return value


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('Root utility for minimiser: 3')
    print('Root utility for maximiser: 3')
    print('----------------------------------')
    game_tree = 3
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('Root utility for minimiser: 1')
    print('Root utility for maximiser: 3')
    print('----------------------------------')
    game_tree = [1, 2, 3]
    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal')
    print('1')
    print('3')
    print('----------------------------------')
    game_tree = [1, 2, [3]]
    print(min_value(game_tree))
    print(max_value(game_tree))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal')
    print('2')
    print('3')
    print('----------------------------------')
    game_tree = [[1, 2], [3]]
    print(min_value(game_tree))
    print(max_value(game_tree))


if __name__ == "__main__":
    main()
