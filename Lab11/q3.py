"""Consider the following explicit game tree.

[2, [-1, 5], [1, 3], 4]

Assuming that the player at the root of the tree is Max, prune the tree (if necessary).
Provide two variables: pruned_tree which is the pruned game tree and pruning_events which is a list of pairs of alpha
and beta, one for each time a pruning event was triggered."""


from math import inf

pruned_tree = [
    2, [-1], [1], 4
]

pruning_events = [
    (2, -1),
    (2, 1),
]


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('[2, [-1], [1], 4]')
    print('[(2, -1), (2, 1)]')
    print('----------------------------------')
    print(pruned_tree)
    print(pruning_events)


if __name__ == "__main__":
    main()
