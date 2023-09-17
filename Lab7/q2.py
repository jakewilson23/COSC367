"""Write a function n_queens_cost(state) that takes a state (a total assignment) for an n-queen problem and returns
the number conflicts for that state. We define the number of conflicts to be the number of unordered pairs of queens
(objects) that threaten (attack) each other. The state will be given in the form of a sequence (tuple more
specifically). The state is a permutation of numbers from 1 to n (inclusive). The value of n must be inferred from
the given state.

Hint: diagonals have a slope of 1 or -1. You want to see if abs(dx)==abs(dy) where dx and dy are, respectively,
the horizontal and vertical distances between a pair of queens. Note that in the representation we have chosen there
won't be any row-wise or column-wise conflict because no two queens can be on the same column or row.

Challenge: you can write this function with a single statement (one return statement in two lines). See
itertools.combinations."""


def n_queens_cost(state):
    num_conflicts = 0
    for queen_col, queen_row in enumerate(state):
        for other_col, other_row in enumerate(state):
            if queen_col != other_col:  # cant conflict with itself
                if abs(queen_col - other_col) == abs(queen_row - other_row):
                    num_conflicts += 1
    return int(num_conflicts / 2)    # in this solution each conflict gets counter twice


def main():
    # Test 1
    print(n_queens_cost((1, 2)))

    # Test 2
    print(n_queens_cost((1, 3, 2)))

    # Test 3
    print(n_queens_cost((1, 2, 3)))

    # Test 4
    print(n_queens_cost((1,)))

    # Test 5
    print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

    # Test 6
    print(n_queens_cost((2, 3, 1, 4)))


if __name__ == "__main__":
    main()
