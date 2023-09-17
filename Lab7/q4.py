"""Write a procedure greedy_descent_with_random_restart(random_state, neighbours, cost) that takes three functions,
one to get a new random state and two to compute the neighbours or cost of a state and then uses greedy_descent (you
wrote earlier) to find a solution. The first state in the search must be obtained by calling the function
random_state. The procedure must print each state it goes through (including the first and last one) in the order
they are encountered. When the search reaches a local minimum that is not global, the procedure must print RESTART
and restart the search by calling random_state. Your procedure will be tested only with optimisation versions of CSP
problems that have a solution.

Arguments

random_state: a function that takes no argument and return a random state; neighbours: a function that takes a state
and returns a list of neighbours; cost a function that takes a state returns its cost (e.g. number of conflicts).
Important: You must also provide your implementation of n_queens_neighbours, n_queens_cost, and greedy_descent from
previous questions. You do not need to implement random_state; it is implemented in test cases."""
from q3 import greedy_descent


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    state = random_state()
    running = True
    while running:
        output = greedy_descent(state, neighbours, cost)
        state_cost = cost(state)
        for descent in output:
            print(descent)
            state_cost = cost(descent)
        if state_cost == 0:
            running = False
        else:
            print("RESTART")
            state = random_state()


def main():
    # Test 1
    import random
    from q1 import n_queens_neighbours as neighbours
    from q2 import n_queens_cost as cost

    N = 6
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1, N + 1), N))

    greedy_descent_with_random_restart(random_state, neighbours, cost)

    # Test 2

    N = 8
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1, N + 1), N))

    greedy_descent_with_random_restart(random_state, neighbours, cost)


if __name__ == "__main__":
    main()
