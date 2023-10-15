"""Consider the following explicit game tree.

[3, [[2, 1], [4, [7, -2]]], 0]

Assuming that the player at the root of the tree is Max, prune the tree (if
necessary). Provide two variables: pruned_tree which is the pruned game tree and pruning_events which is a list of
pairs of alpha and beta, one for each time a pruning event was triggered."""


from math import inf

pruned_tree = [
    3, [[2, 1]], 0
]

pruning_events = [
    (3, 2)
]


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('[3, [[2, 1]], 0]')
    print('[(3, 2)]')
    print('----------------------------------')
    print(pruned_tree)
    print(pruning_events)


if __name__ == "__main__":
    main()
