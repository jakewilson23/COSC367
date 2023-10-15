"""Write two functions max_action_value(game_tree) and min_action_value(game_tree) that given a game tree,
return a pair where first element is the best action and the second element is the utility of the root of the tree
when the root is a max node or min node correspondingly. For a leaf node the action is None; for an internal node,
the action is the index of the subtree corresponding to the best action. Process the children of a node from left (
lower index) to right (higher index). If there is a tie, return the left-most optimal action."""


def max_action_value(game_tree):
    if isinstance(game_tree, int):
        return None, game_tree
    action = 0
    value = float("-inf")
    for index, child in enumerate(game_tree):
        _, child_value = min_action_value(child)
        if child_value > value:
            value = child_value
            action = index
    return action, value


def min_action_value(game_tree):
    if isinstance(game_tree, int):
        return None, game_tree
    action = 0
    value = float("inf")
    for index, child in enumerate(game_tree):
        _, child_value = max_action_value(child)
        if child_value < value:
            value = child_value
            action = index
    return action, value


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('Best action if playing min: 1')
    print('Best guaranteed utility: 1')
    print('')
    print('Best action if playing max: 2')
    print('Best guaranteed utility: 4')
    print('----------------------------------')
    game_tree = [2, [-3, 1], 4, 1]
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('Best action if playing min: None')
    print('Best guaranteed utility: 3')
    print('')
    print('Best action if playing max: None')
    print('Best guaranteed utility: 3')
    print('----------------------------------')
    game_tree = 3
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal')
    print('Best action if playing min: 0')
    print('Best guaranteed utility: 1')
    print('')
    print('Best action if playing max: 2')
    print('Best guaranteed utility: 3')
    print('----------------------------------')
    game_tree = [1, 2, [3]]
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)


if __name__ == "__main__":
    main()
