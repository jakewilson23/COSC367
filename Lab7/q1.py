"""Write a function n_queens_neighbours(state) that takes a state (total assignment) for an n-queen problem and
returns a sorted list of states that are the neighbours of the current assignment. A neighbour is obtained by
swapping the position of two numbers in the given permutation.

Like before, the state will be given in the form of a sequence (more specifically, a tuple). The state is a
permutation of numbers from 1 to n (inclusive). The value of n must be inferred from the given state. The time
complexity of your solution must be in O(n3) . [Ignoring the cost of constructing n-tuples (i.e. if it took constant
time), the complexity would be O(n2) .]This means that you should not generate all possible permutations of n.

Because of the choice of representation (the permutation of numbers from 1 to n) the concept of neighbourhood in this
question is different from that in the examples given in the lecture notes. The representation we use here does not
allow repeated numbers in a sequence, therefore we define a neighbouring assignment to be one that can be obtained by
swapping the position of two numbers in the current assignment.

Note the spelling of neighbours. Also note that the neighbours of an assignment do not include the assignment itself.

Hint: A very simple way of implementing this function is to write two nested for loops and swapping the elements in
the given permutation. Since tuples are immutable, you can temporarily convert them to a list to perform the swap and
then convert them back to tuple.

Challenge: you can write this function with a single statement (one return statement in two lines). See
itertools.combinations."""
from itertools import combinations


def n_queens_neighbours(state):
    result = []
    for first_index, first_swap in enumerate(state):
        for second_index, second_swap in enumerate(state):
            if first_swap != second_swap:
                new_neighbour = list(state)
                new_neighbour[first_index], new_neighbour[second_index] = new_neighbour[second_index], \
                    new_neighbour[first_index]
                new_neighbour = tuple(new_neighbour)
                if new_neighbour not in result:
                    result.append(new_neighbour)
    return sorted(result)


def main():
    # Test 1
    print(n_queens_neighbours((1, 2)))

    # Test 2
    print(n_queens_neighbours((1, 3, 2)))

    # Test 3
    print(n_queens_neighbours((1, 2, 3)))

    # Test 4
    print(n_queens_neighbours((1,)))

    # Test 5
    for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)

    # Test 6
    for neighbour in n_queens_neighbours((2, 3, 1, 4)):
        print(neighbour)


if __name__ == "__main__":
    main()
