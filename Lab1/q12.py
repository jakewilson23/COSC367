import collections

from search import *
import copy

BLANK = ' '


class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""

        n = len(state)  # the size of the puzzle

        # Find i and j such that state[i][j] == BLANK
        for row_num, items_in_row in enumerate(state):
            for col_num, item_in_row in enumerate(items_in_row):
                if item_in_row == BLANK:
                    i, j = row_num, col_num

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])  # or blank goes right
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""

        n = len(state)
        answer_list = []
        for row in state:
            for item in row:
                answer_list.append(item)

        answer = True
        for count, item in enumerate(answer_list):
            if count != 0:
                if item != count:
                    answer = False
        return answer


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            top_of_queue = self.container.popleft()
            return top_of_queue
        else:
            raise StopIteration  # don't change this one

def main():
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, ' ']])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    graph = SlidingPuzzleGraph([[3, ' '],
                                [1, 2]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    graph = SlidingPuzzleGraph([[1, ' ', 2],
                                [6, 4, 3],
                                [7, 8, 5]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

if __name__ == "__main__":
    main()